# Imports

# Django imports
from django.contrib import admin

# Internal Imports
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin Class for Contact Model
    """
    list_display = (
        'name',
        'reason',
        'body',
        'email'
        )
    list_filter = (
        'name',
        'reason',
        'email'
        )
    search_fields = (
        'name',
        'email',
        )
