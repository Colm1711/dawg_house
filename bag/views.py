# Imports

# Djanog Imports
from django.shortcuts import render


def view_bag(request):
    """
    A view that renders the bag contents page
    of bookings
    """
    return render(request, 'bag.html')
