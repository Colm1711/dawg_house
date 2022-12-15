# Imports

# Django imports
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic
from django.contrib import messages
# Internal imports
from .models import Service, Size, Breed, Comment
from .forms import ServiceForm


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


def service_comments(request, slug):
    """ A view to show individual service details """

    service = get_object_or_404(Service, slug=slug)
    reviews = Comment.objects.filter(service=service.id)

    context = {
        'service': service,
        'reviews': reviews,
    }

    return render(request, 'services/add_review.html', context)


@staff_member_required
def add_service(request):
    """ Add a new service to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Hey, you are not authorised to be down here!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added a new service')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add the new service'
                                    'please check if form is valid')
    else:
        form = ServiceForm()
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_service(request, slug):
    """ Edit an existing service """
    service = get_object_or_404(Service, slug=slug)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save()
            messages.success(request, f'Successfully updated {service.name}!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.info(request, f'Failed to update\
                           {service.name}. Please ensure valid form.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.service_type}')

        template = 'services/edit_service.html'
        context = {
            'form': form,
            'service': service
        }

        return render(request, template, context)


@staff_member_required
def delete_service(request, slug):
    """ Delete service from site """
    service = get_object_or_404(Service, slug=slug)
    service.delete()
    messages.success(request, f'{service.name}has been deleted permanently')
    return redirect(reverse('services'))
