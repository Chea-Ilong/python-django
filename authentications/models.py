
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Make email unique for authentication
    email = models.EmailField(unique=True)
    
    # Custom fields
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_vendor = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
