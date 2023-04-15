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
    """Custom user model with email as the username field."""

    ROLE_CHOICES = (("student", "Student"), ("teacher", "Teacher"))
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    profile_cover = models.ImageField(upload_to='profile_covers/', null=True, blank=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    introduction = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "role"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """Save the user and check for email uniqueness."""
        try:
            existing_user = CustomUser.objects.get(email=self.email)
            if existing_user and existing_user.pk != self.pk:
                raise ValidationError("A user with this email already exists.")
        # If no user is found, pass and continue to save the user
        except CustomUser.DoesNotExist:
            pass

        super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
