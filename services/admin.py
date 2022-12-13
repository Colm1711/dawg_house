from django.contrib import admin
from .models import Size, Service


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'additional_fee'
    )

    ordering = ('additional_fee',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_type',
        'sub_heading',
        'cost'
    )

    ordering = ('service_type',)


admin.site.register(Size)
admin.site.register(Service)
