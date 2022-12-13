from django.shortcuts import render, get_object_or_404
from .models import Service, Size, Breed


def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ A view to show individual service details """

    service = get_object_or_404(Service, pk=service_id)
    breeds = Breed.objects.order_by('breed')
    sizes = Size.objects.all()

    context = {
        'service': service,
        'breeds': breeds,
        'sizes': sizes,
    }

    return render(request, 'services/service_detail.html', context)
