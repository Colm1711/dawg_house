# Imports
from datetime import datetime

# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

# Internal imports
from .forms import BookingForm


def booking_form(request):
    """
    This function handles rendering of the update page to the user
    and logic to update.
    User must be signed in to do this.
    """

    success_message = 'Your booking has been processed successfully'
    template = 'booking_form.html'
    form = BookingForm(request.POST)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.price = form.service_provider_id.price_per_service
        form.total = (get_total_num_of_days(form.start_date, form.end_date) *
                      form.price)
        form.save()
        messages.success(request, success_message)
        return redirect('/')

    # pass forms to the html form
    context = {'form': BookingForm,
               'stripe_public_key': stripe_public_key,
               'client_secret': 'test client secret',
               }

    return render(request, template, context)


def get_total_num_of_days(start, end):
    """
    Function to calculate the number of days in date range
    selected by the user.

    start = the start date selected
    end = the end date slected

    if start and end are the same then one day is default
    """
    total = (datetime.strptime(str(end), "%Y-%m-%d") -
             datetime.strptime(str(start), "%Y-%m-%d")).days
    if total == 0:
        num_days = 1
    else:
        num_days = total
    return num_days
