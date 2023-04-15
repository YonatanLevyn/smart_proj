"""
forms.py

This file contains the forms for the user_management app.
At the moment, there is only one form, the IntroductionForm,
which allows users to update their introduction text in their profile.
"""
from django import forms
from .models import CustomUser

class IntroductionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['introduction']
        
class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_photo']

class CoverPhotoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_cover']
