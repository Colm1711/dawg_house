# Imports

# Django imports
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

# Internal imports
from .models import Service, Size, Breed
from .forms import BreedForm


def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, slug):
    """ A view to show individual service details """

    service = get_object_or_404(Service, slug=slug)
    breeds = Breed.objects.order_by('breed')
    sizes = Size.objects.all()

    context = {
        'service': service,
        'breeds': breeds,
        'sizes': sizes,
    }

    return render(request, 'services/service_detail.html', context)


@staff_member_required
def add_breed(request):
    """Form to add new dog breed to site"""

    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            breed = form.save
            messages.success(request, 'Successfully added a new breed')
            return redirect(reverse('services'), argrs=[breed.id])
        else:
            messages.info(request,
                          'Failed to add the breed, please check the form!')
    else:
        form = BreedForm()
        template = 'services/add_breed.html'
    context = {
        'form': form
    }

    return render(request, template, context)
