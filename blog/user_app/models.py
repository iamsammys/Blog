from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """User Profile Model
    
    Arguments:
        models {Model} -- Model class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, default="I am subscriber of ScholarSpectrum app")
    birth_date = models.DateField(blank=True, null=True, default="2000-01-01")
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.png')

    def __str__(self):
        """Return user name
        
        Returns:
            str -- User name
        """
        return self.user.username