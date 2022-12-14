# Imports
import uuid

# Django imports
from django.db import models
from django.db.models import Sum

# Internal imports
from services.models import Service
from profiles.models import UserProfile


class ServiceOrder(models.Model):
    order_number = models.CharField(max_length=2, null=False, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,
                             blank=True, related_name='orders')
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    address_1 = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=False)
    eircode = models.CharField(max_length=7, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    created_on = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default="")

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_order_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        sum = (self.lineitem.aggregate((Sum('lineitem_total'))
               ['lineitem_total__sum']) or 0)
        self.order_total = sum
        self.save

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't already been set
        """

        if not self.order_number:
            self.order.number = self._generate_booking_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(ServiceOrder, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='orderlineitems')
    service = models.ForeignKey(Service, null=False, blank=False,
                                on_delete=models.CASCADE)
    breed = models.CharField(max_length=40, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.service.cost * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.service.sku} on order {self.order.order_number}'
