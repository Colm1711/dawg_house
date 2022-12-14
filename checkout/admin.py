# Imports

# Django imports
from django.contrib import admin

# Internal imports
from .models import ServiceOrder, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline class for OrderLineItem
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    """
    A class for Service Order Admin

    Lists how the content is presetned to the Admin User and
    provides List filter panel.
    """

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'created_on',
        'order_total',
        'original_bag',
        'stripe_pid'
    )

    fields = (
        'order_number',
        'user',
        'created_on',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address_1',
        'address_2',
        'county',
        'eircode',
        'order_total',
        'original_bag',
        'stripe_pid'
    )

    list_display = (
        'order_number',
        'created_on',
        'first_name',
        'last_name',
        'order_total',
        )

    ordering = ('-created_on',)
