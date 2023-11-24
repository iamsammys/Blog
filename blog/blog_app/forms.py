from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """Form for creating a post
    
    Attributes:
        forms.ModelForm: form for creating a post
    """
    class Meta:
        """Meta class for PostForm"""
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"})
        }