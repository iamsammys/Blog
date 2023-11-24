from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile

    Arguments:
        sender {User} -- User model
        instance {User} -- User instance
        created {bool} -- True if created
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, created, instance, **kwargs):
    """Save user profile

    Arguments:
        sender {User} -- User model
        instance {User} -- User instance
    """
    if created:
        instance.userprofile.save()