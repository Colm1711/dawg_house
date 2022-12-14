# Imports

# Django imports
from django.shortcuts import get_object_or_404

# Internal imports
from services.models import Service


def bag_contents(request):
    """
    Function to return the bag contents to user.
    """
    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for service_id, bag_data in bag.items():
        service = get_object_or_404(Service, pk=service_id)
        for breed, quantity in bag_data['items_by_breed'].items():
            total += quantity * service.cost
            service_count += quantity
            bag_items.append({
                'service_id': service_id,
                'quantity': quantity,
                'service': service,
                'breed': breed,
            })
    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
    }

    return context
