# Imports

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Internal imports
from .forms import ServiceOderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, "There's nothing to checkout")
        return redirect('services')

    order_form = ServiceOderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
