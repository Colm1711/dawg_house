# Imports

# Djanog Imports
from django.shortcuts import render, redirect

# INternal imports
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

    if service_id in list(bag.keys()):
        bag[service_id] = quantity
    else:
        bag[service_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
