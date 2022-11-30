from django.contrib import admin
from .models import UserProfile, ServiceProvider


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
    'Account Created On'
    'Account Updated On'
    """
    list_display = ('first_name', 'last_name', 'phone_number', 'address_1',
                    'address_2', 'county', 'eircode', 'is_service_provider',
                    'acc_created_on', 'acc_updated_on')
    search_fields = ['first_name', 'last_name', 'phone_number', 'address_1',
                     'address_2', 'county', 'eircode', 'is_service_provider',
                     'acc_created_on', 'acc_updated_on']
    list_filter = ('first_name', 'last_name', 'phone_number', 'address_1',
                   'address_2', 'county', 'eircode', 'is_service_provider',
                   'acc_created_on', 'acc_updated_on')


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    """
    This class controls the Admin view of Users

    Lists how the content is presetned to the Admin User and
    provides List filter panel.

    Search item fields:
    'Service Type'
    'Total Occupancy'
    'Description'
    'Has fence'
    'Pets allowed in House'
    'Owner has dog'
    'Owner has cat'
    'Owner has children'

    """
    list_display = ('service_type', 'total_occupancy', 'description',
                    'has_fenced_garden', 'pet_allowed_in_house',
                    'owner_has_dog', 'owner_has_cat', 'owner_has_children')
    search_fields = ['service_type', 'total_occupancy', 'description',
                     'has_fenced_garden', 'pet_allowed_in_house',
                     'owner_has_dog', 'owner_has_cat', 'owner_has_children']
    list_filter = ('service_type', 'total_occupancy', 'description',
                   'has_fenced_garden', 'pet_allowed_in_house',
                   'owner_has_dog', 'owner_has_cat', 'owner_has_children')
