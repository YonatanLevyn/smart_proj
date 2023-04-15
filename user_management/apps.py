"""
apps.py

This file contains the configuration for the user_management app.
It defines a single class, UserManagementConfig, which inherits from AppConfig
and sets some default settings for the app.
"""
from django.apps import AppConfig

class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # Use 64-bit integer for primary keys instead of the default 32-bit
    name = 'user_management'
