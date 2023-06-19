"""
User management models.

This file contains the models for the user_management app.
At the moment, there is only one model, the CustomUser model,
which is a custom user model that extends the AbstractBaseUser
model provided by Django. This model is used to store user data
such as email, username, role, introduction text, etc.
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    """Custom user manager for creating users and superusers."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # email is the primary identifier for a user and is used for authentication
    # if the email is not unique, an error will be thrown, preventing the user from being created
    # if the email is unique, the user will be created and saved to the database
    email = models.EmailField(unique=True)
    role = models.CharField(null=True, max_length=255, default="user")
    username = models.CharField(max_length=255)
    # null=True allows the field to be null in the database, blank=True allows the field to be blank in forms
    introduction = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # objects is a CustomUserManager object that is used to create and save users
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


    # Meta class is used to provide metadata about the CustomUser model
    # In this case, we are providing the verbose name and verbose name plural
    # This is used to display the model name in the admin panel
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
