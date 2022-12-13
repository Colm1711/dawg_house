# Imports

# Djanog Imports
from django.shortcuts import render, redirect
from django.contrib import messages

# Internal imports
from services.models import Service, Breed, Size


def view_bag(request):
    """
    A view that renders the bag contents page
    of bookings
    """
    return render(request, 'bag.html')


def add_to_bag(request, service_id):
    """
    Add a service to the shopping cart
    """
    service = Service.objects.get(pk=service_id)
    breed = request.POST['breed_selector']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if breed:
        if service_id in list(bag.keys()):
            if breed in bag[service_id]['items_by_breed'].keys():
                bag[service_id]['items_by_breed'][breed] += quantity
                messages.info(request,
                              (f'We have updated {quantity}\
                              {service.service_type} for your dog of choice\
                              {breed}'))
            else:
                bag[service_id]['items_by_breed'][breed] = quantity
                messages.success(request, (f'We have added {quantity}\
                                {service.service_type} for your dog of\
                                 choice {breed}'))
        else:
            bag[service_id] = {'items_by_breed': {breed: quantity}}
            messages.error(request, 'Please pick a breed!')
    else:
        messages.error(request, 'You need to select your dogs breed!')

    request.session['bag'] = bag
    return redirect(redirect_url)
