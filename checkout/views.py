# Imports
import stripe

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
# Internal imports
from .forms import ServiceOderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, "There's nothing to checkout")
        return redirect('services')

    order_form = ServiceOderForm
    template = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
