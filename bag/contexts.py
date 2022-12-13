# Imports

# Django imports
from django.shortcuts import get_object_or_404

# Internal imports
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
