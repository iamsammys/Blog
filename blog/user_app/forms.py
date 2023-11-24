from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    """Form for registering a user
    
    Attributes:
        UserCreationForm: form for creating a user
    """
    email = forms.EmailField()
    
    class Meta:
        """Meta class for UserRegistrationForm"""
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    """Form for updating a user
    
    Attributes:
        forms.ModelForm: form for updating a user
    """
    email = forms.EmailField()

    class Meta:
        """Meta class for UserUpdateForm"""
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class ProfileUpdateForm(forms.ModelForm):
    """Form for updating a profile
    
    Attributes:
        forms.ModelForm: form for updating a profile
    """
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        """Meta class for ProfileUpdateForm"""
        model = UserProfile
        fields = ["image", "bio", "birth_date"]