# Imports

# Django imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Cloudinary import
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    information, user verification and profile update details.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='userprofile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    acc_created_on = models.DateTimeField(auto_now_add=True)
    acc_updated_on = models.DateTimeField(auto_now=True)
    is_service_provider = models.BooleanField(default=False)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.email


# defining signal methods to run post save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
