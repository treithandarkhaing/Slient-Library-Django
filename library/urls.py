from . import views
from django.urls import path

urlpatterns = [
    #Book Management URLs
    path('books/', views.book_list, name='book_list'),   
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'),   
    path('create/', views.book_create, name='book_create'), 
    path('update/<int:pk>/', views.book_update, name='book_update'),

    #Home Page URL
    path('', views.home, name='home'),

    #User Management URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),  
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('admin/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/users/add/', views.user_create, name='user_create'),
    path('admin/users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('admin/users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
]