# Imports

# Django imports
from django.db import models


class Contact(models.Model):
    """
    A class for the contact us model
    """
    class Reason(models.TextChoices):
        Booking = "1", "I have a query on a Booking"
        Service_Provider = "2", "I have query on becoming Service Provider"
        Other = "3", "All Other Queries"

    reason = models.CharField(
        max_length=2, choices=Reason.choices,
        default=Reason.Booking)
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    email = models.EmailField(max_length=70)
    creation_date = models.DateField(auto_now=True)
    is_replied = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name
