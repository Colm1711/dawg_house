# Imports

# Djanog Imports
from django.shortcuts import render, redirect, reverse, HttpResponse
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
                              {breed} with another'))
            else:
                bag[service_id]['items_by_breed'][breed] = quantity
                messages.success(request, (f'We have added {quantity}\
                                {service.service_type} for your dog of\
                                 choice {breed}'))
        else:
            bag[service_id] = {'items_by_breed': {breed: quantity}}
            messages.success(request, (f'We have added {quantity}\
                              {service.service_type} for your dog of choice\
                              {breed} with another'))
    else:
        messages.warning(request, 'You need to select your dogs breed!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, service_id):
    """ Adjust a service in the shopping cart bag """

    service = Service.objects.get(pk=service_id)
    quantity = int(request.POST.get('quantity'))
    breed = request.POST['breed_selector']
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[service_id]['items_by_breed'][breed] = quantity
        messages.success(request, f'We have updated {service.service_type} for\
                                    {breed} to {quantity}')
    else:
        del quantity
        messages.warning(request, f'0 is not a valid selection. Why not try\
                                    the remove button? :)')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, service_id):
    """ Remove a service from the bag """
    try:
        breed = request.POST['breed']
        bag = request.session.get('bag', {})

        del bag[service_id]['items_by_breed'][breed]

        request.session['bag'] = bag
        messages.warning(request, f'You have removed the service for {breed}')
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
