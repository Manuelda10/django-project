from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = None # We don't need username field, but AbstractUser has it by default

    USERNAME_FIELD = 'email' #This is to login with email and password
    REQUIRED_FIELDS = []

    
