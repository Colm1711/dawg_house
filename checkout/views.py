# Imports
import stripe
import json

# Django imports
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

# Internal imports
from services.models import Service
from .models import ServiceOrder, OrderLineItem
from .forms import ServiceOderForm
from bag.contexts import bag_contents


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'county': request.POST['county'],
            'eircode': request.POST['eircode'],
        }
        order_form = ServiceOderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            print(pid)
            # order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order_form.save()
            for service_id, item_data in bag.items():
                try:
                    service = get_object_or_404(Service, pk=service_id)
                    for breed, quantity in item_data['items_by_breed'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            service=service,
                            breed=breed,
                            quantity=quantity,
                        )
                        print()
                        order_line_item.save()
                except ServiceOrder.DoesNotExist:
                    messages.info(request, (
                        "One of the services in your cart wasn't found in our\
                         database."
                        "Please try again!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', 
                            args=[order.order_number]))
    else:
        print('Here else')
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


def checkout_success(request, order_number):
    """ A view to return the success page"""
    template = 'checkout/checkout_success.html'
    return render(request, template)
