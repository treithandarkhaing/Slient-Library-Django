from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_pic = models.ImageField(upload_to='cover_pics/', blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=50)
    published_date = models.DateField()
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return str(self.user) + "[" + str(self.bio) + "]" + "[" + str(self.profile_pic) + "]"