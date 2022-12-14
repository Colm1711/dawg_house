# Imports


# Django imports
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Internal imports
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the total on lineitem update/create
    """
    instance.order.update_total()
