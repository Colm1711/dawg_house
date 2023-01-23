# Imports

# Django imports
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    """
    A model to hold the services that are on offer to
    the user to book.

    Contains Type, length, cost and destails
    """
    service_type = models.CharField(max_length=254)
    service_length = models.CharField(max_length=254)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    sub_heading = models.CharField(max_length=254)
    detail_1 = models.CharField(max_length=254)
    detail_2 = models.CharField(max_length=254)
    description = models.TextField(max_length=1000,
                                   null=True,
                                   blank=True,)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Generate a slug for service.
        """
        if not self.slug and self.service_type:
            self.slug = slugify(self.service_type)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        A method to return the absolute url of service
        """
        return reverse('service_detail', args=[str(self.slug)])

    def __str__(self):
        return self.service_type


class Size(models.Model):
    """
    A model to hold the sizes of dog.

    Contains Name size and additional cost that incurs.
    """
    name = models.CharField(max_length=254)
    additional_fee = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Breed(models.Model):
    """
    A model to hold the dog breeds.

    Contains Breed name and is linked to sizes.
    """
    size = models.ForeignKey('Size', null=True, blank=True,
                             on_delete=models.SET_NULL)
    breed = models.CharField(max_length=254)

    def __str__(self):
        return self.breed


class Comment(models.Model):
    """
    This is the review model for services for user to leave a review
    on a service to let others know thoughts.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    comment = models.TextField(max_length=254, null=False, blank=False)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review {self.comment} by {self.name}"
