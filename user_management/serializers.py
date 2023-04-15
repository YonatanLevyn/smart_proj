"""
serializers.py

This file contains the serializers for the user_management app.
We are using Django Rest Framework (DRF) based APIs in this case since the communication is
primarily with web browsers. Web browsers natively support JSON format, making DRF a suitable
choice for the front-end and back-end communication.
"""
from rest_framework import serializers
from .models import CustomUser

# Serializer for handling CustomUser data without the password field
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "role"]

# Serializer for handling CustomUser data during user registration, including the password field
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "role", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    # Overriding the create method to use CustomUserManager's create_user method
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            username=validated_data["name"],
            role=validated_data["role"],
            password=validated_data["password"],
        )
        return user

