from django.shortcuts import redirect, render
from .models import Book
from django.shortcuts import get_object_or_404
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your views here.

#Home
def home(request):
    # Logic for the home page
    message = "Welcome to the Library Management System"
    return render(request, 'home.html', {'message': message})

#Books 
#View Function
def book_list(request):   
    # Logic to retrieve and display a list of books
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

#Delete Function
def book_delete(request, book_id):
    # Logic to delete a specific book by its ID
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        # Make sure 'book_list' matches the name in your urls.py exactly
        return redirect('book_list')
    
    return render('book_list')

# This function checks if the user is an admin
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def user_dashboard(request):
    users = User.objects.all().order_by('-date_joined')
    stats = {
        'total': users.count(),
        'staff': users.filter(is_staff=True).count(),
        'recent': users.filter(is_active=True).count(),
    }
    return render(request, 'user_dashboard.html', {'users': users, 'stats': stats})

@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New user created successfully!")
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'user_form.html', {'form': form, 'title': 'Add New User'})

@user_passes_test(is_admin)
def user_edit(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # Using a simplified form for admin updates
        target_user.email = request.POST.get('email')
        target_user.first_name = request.POST.get('first_name')
        target_user.last_name = request.POST.get('last_name')
        target_user.is_staff = 'is_staff' in request.POST
        target_user.save()
        messages.success(request, f"User {target_user.username} updated!")
        return redirect('user_dashboard')
    return render(request, 'user_edit_form.html', {'target_user': target_user})

#Update Function
@user_passes_test(is_admin) # Only admins can enter here
def book_update(request, pk):
    # 1. Get the specific book or show a 404 error if not found
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        # 2. Use the BookForm but 'instance=book' tells it to update the existing one
        form = BookForm(request.POST, request.FILES, instance=book)
        
        if form.is_valid():
            form.save()
            messages.success(request, f"'{book.title}' updated successfully!")
            return redirect('book_list')
    else:
        # 3. Show the form with the book's current data already filled in
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {
        'form': form,
        'title': 'Update Book' # We can use this to change the heading in the HTML
    })

#Create Function
def book_create(request):
    # Logic to create a new book entry
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'book_form.html', {'form': form})

#------User Functionalities------
#Register User
def register(request):
    if request.method == 'POST':

        #User Table Fields
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        #Profile Table Fields
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic')

        # Validate User - Duplicate Username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'register.html')
        
        # Validate Password Match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'register.html')
        
        # Create User
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        profile, created = Profile.objects.get_or_create(user=user)
        profile.bio = bio
        profile.profile_pic = profile_pic
    
        # Create User Profile
        # profile = Profile.objects.create(
        #     user=user,
        #     bio=bio,
        #     profile_pic=profile_pic
        # )

        #user.save()
        profile.save()
        messages.success(request, 'Registration successful. You can now log in.')

        return redirect('login')
    return render(request, 'register.html')


#Login User
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            # if user.is_superuser:
            #     return redirect('/')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

#Logout User
def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required(login_url='login')
#View User Profile
def profile(request):
    #return render(request, 'profile.html')

    #profile = request.user.profile  # or Profile.objects.get_or_create(user=request.user)[0]
    # Instead of request.user.profile, we use "get_or_create"
    # This means: "Find the profile, but if it's missing, build a new one right now"
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Get form data
        bio = request.POST.get('bio', '').strip()
        profile_pic = request.FILES.get('profile_pic')

        # Update fields
        profile.bio = bio
        
        if profile_pic:
            profile.profile_pic = profile_pic

        # This is the important line you're missing or need to confirm
        profile.save()

        messages.success(request, "Your profile has been updated successfully.")
        return redirect('profile')  # or wherever you want to redirect

    # GET request → show the current profile data
    context = {
        'profile': profile,
        # If you're using forms, you could pass a form here instead
    }
    return render(request, 'profile.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, user_id):
    if request.method == 'POST':
        user_to_delete = get_object_or_404(User, id=user_id)
        if user_to_delete == request.user:
            messages.error(request, "You cannot delete your own admin account.")
        else:
            user_to_delete.delete()
            messages.success(request, "User deleted successfully.")
    return redirect('user_dashboard')