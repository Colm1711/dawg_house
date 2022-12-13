from django.contrib import admin
from .models import Size, Service, Breed


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
