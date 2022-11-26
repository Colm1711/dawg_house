from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    This class controls the Admin view of Users

    Lists how the content is presetned to the Admin User and
    provides List filter panel.

    Search item fields:
    'First Name'
    'Last Name'
    'Phone Number'
    'Email'
    'Is Service Provider'
    """
    list_display = ('first_name', 'last_name', 'phone_number',
                    'is_service_provider')
    search_fields = ['first_name', 'last_name', 'phone_number',
                     'is_service_provider']
    list_filter = ('first_name', 'last_name', 'phone_number',
                   'is_service_provider')
