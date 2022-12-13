# Imports

# Django imports
from django.shortcuts import get_object_or_404

# Internal imports
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for service_id, quantity in bag.items():
        service = get_object_or_404(Service, pk=service_id)
        service_count += quantity * service.cost
        bag_items.append({
            'service_id': service_id,
            'quantity': quantity,
            'service': service,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
