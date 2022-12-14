# Imports
import stripe
import json

# Django imports
from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404,
                              HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Internal imports
from services.models import Service
from .models import ServiceOrder, OrderLineItem
from .forms import ServiceOderForm
from bag.contexts import bag_contents
from profiles.forms import RegisterForm
from profiles.models import UserProfile


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ A view to return the success page"""
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
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
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
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
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
        messages.info(request, 'Stripe public key is missing. \
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

    save_info = request.session.get('save_info')
    order = get_object_or_404(ServiceOrder, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'first_name': order.first_name,
                'last_name': order.last_name,
                'email': order.email,
                'phone_number': order.phone_number,
                'address_1': order.address_1,
                'address_2': order.address_2,
                'county': order.county,
                'eircode': order.eircode,
            }
            user_profile_form = RegisterForm(profile_data, initial=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                subject = order.order_number
                message = f'Hi {order.first_name} Thanks you have succesfully\
                ordered from Dawghose your {order.order_number} is with our\
                team and will be followed up soon one of our service providers\
                !'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [order.email]
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, f'Order successfully processed! \
                 Your order number is {order_number}. A confirmation \
                email will be sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
