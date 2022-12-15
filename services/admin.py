# Imports

# Django imports
from django.contrib import admin

# Internal imports
from .models import Size, Service, Breed, Comment


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """
    This class controls the Admin view of Breed Sizes

    Lists how the content is presetned to the Admin User and
    provides ordering on fees.

    """
    list_display = (
        'name',
        'additional_fee'
    )

    ordering = ['additional_fee']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    This class controls the Admin view of Services

    Lists how the content is presetned to the Admin User and
    provides ordering on service type.

    """
    list_display = (
        'service_type',
        'sub_heading',
        'cost'
    )

    ordering = ['service_type']


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """
    This class controls the Admin view of Breeds

    Lists how the content is presetned to the Admin User and
    provides List filter panel and provides ordering.

    Search item fields:
    'breed'
    'size'

    """
    list_display = (
        'breed',
        'size'
    )

    search_fields = ['breed', 'size']
    list_filter = ('breed', 'size')
    ordering = ['breed']


@admin.register(Comment)
class ReviewAdmin(admin.ModelAdmin):
    """
    This is the class that controls the Admins view of the
    reviews.
    List how the content is presented to Amdmin User and provides list filter
    panel.
    Provides search fields: 'email', 'comment'
    """
    list_display = ('email', 'comment', 'service', 'created_on',
                    'is_approved')
    list_filter = ('is_approved', 'created_on')
    search_fields = ('email', 'comment')
    actions = ['approve_reviews']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
