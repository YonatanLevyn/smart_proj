
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'username', 'introduction', 'is_active', 'is_staff']
        read_only_fields = ['email', 'is_active', 'is_staff']


# Serializer for handling CustomUser data during user registration, including the password field
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "introduction", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    # Overriding the create method to use CustomUserManager's create_user method
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            introduction=validated_data["introduction"],
        )
        return user

