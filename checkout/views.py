# Imports
import stripe

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
# Internal imports
from .forms import ServiceOderForm
from bag.contexts import bag_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, "There's nothing to checkout")
        return redirect(reverse('services'))

    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    order_form = ServiceOderForm
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = ServiceOderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
