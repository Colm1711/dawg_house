# Imports

# Django imports
from django.db import models
from django.contrib.auth.models import User
from profiles.models import ServiceProvider, UserProfile


class ServiceBooking(models.Model):
    """
    This is the class to store the data of the booking.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider_id = models.ForeignKey(ServiceProvider,
                                            on_delete=models.CASCADE)
    booking_number = models.CharField(max_length=32, null=False,
                                      editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    service_provider_approved = models.BooleanField(default=False)
    mod_is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id.email} | date: {self.date} | time: {self.time}"
