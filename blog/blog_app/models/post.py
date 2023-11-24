from django.db import models
from django.contrib.auth.models import User
from .basemodel import BaseModel
from django.urls import reverse


class Post(BaseModel):
    """Model for blog posts.
    
    Attributes:
        title: title of post
        content: content of post
        date_posted: date post was created
    """
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return string representation of Post object."""
        return "[{}] <{}> {}".format(self.__class__.__name__, self.id, self.title)
    
    def get_absolute_url(self):
        """Return absolute url for Post object.
        
        Returns:
            str: absolute url for Post object
        """
        return reverse("blog_app:post-detail", kwargs={"pk": self.id})