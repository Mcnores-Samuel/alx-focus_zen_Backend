"""This module contains the User model class"""
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """This class defines the custom user manager class"""
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user

        Args:
            email (str): The email address of the user
            password (str): The password of the user
            **extra_fields: Additional fields to be saved in the database

        Returns:
            User: The created user
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Create a superuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    

class UserProfile(AbstractUser):
    """The UserProfile model represents the users of the application. It includes
    fields to store relevant information about each user, such as their name and
    email address

    Args:
        AbstractUser (class): The base user class

    Returns:
        UserProfile: The user profile model
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']