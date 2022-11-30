# Imports

# Django imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Cloudinary import
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    information, user verification and profile update details.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='userprofile')
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    address_1 = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=False)
    eircode = models.CharField(max_length=7, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
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


class ServiceProvider(models.Model):
    """"
    This model holds the information if user
    is a kennel owner, dog sitter or dog walker.

    """
    # defining service type choices
    SERVICE_TYPE_CHOICES = (
      (1, 'Kennel Boarding'),
      (2, 'Pet Setting'),
      (3, 'Dog walking'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='serviceprovider')
    slug = models.SlugField(max_length=200, unique=True)
    service_type = models.PositiveSmallIntegerField(
                                                choices=SERVICE_TYPE_CHOICES,
                                                blank=False, null=False)
    total_occupancy = models.IntegerField()
    price_per_service = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16,
                                    blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16,
                                   blank=True, null=True)
    has_fenced_garden = models.BooleanField(default=False)
    non_smoking = models.BooleanField(default=False)
    pet_allowed_in_house = models.BooleanField(default=False)
    owner_has_dog = models.BooleanField(default=False)
    owner_has_cat = models.BooleanField(default=False)
    owner_has_children = models.BooleanField(default=False)

    # will check if a service provider exists in model DB and if it does
    # will increment add underscore and increment the slug number counter by 1
    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.service_type)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = ServiceProvider.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except ServiceProvider.DoesNotExist:
                    self.slug = slug
                    break
        super(ServiceProvider, self).save(*args, **kwargs)
