from django.db import models


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
    description = models.TextField()

    def __str__(self):
        return self.service_type
