from django.contrib import admin
from .models import Book  # Import your models here
from .models import Profile  # Import Profile model

# Register your models here.
#admin.site.register(Book) # Replace ... with your model names to register them in the admin site.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cover_pic')  # Customize as per your model fields

    search_fields = ('title', 'author')  # Customize as per your model fields

    list_filter = ('title','published_date')  # Customize as per your model fields

admin.register(Profile)  # Register Profile model in the admin site