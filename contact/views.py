# Imports

# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
# Internal imports
from .forms import ContactForm


def contact_us(request):
    """
    A function to display contact us page with contact form,
    get contact details and save to model
    """
    contact_form = ContactForm()
    if request.method == 'GET':
        if not request.user.is_authenticated:
            contact_form = ContactForm()
        elif request.user.userprofile:
            contact_form = ContactForm(
                initial={
                    'email': request.user.email,
                        }
                )
        else:
            contact_form = ContactForm(
                initial={
                    'email': request.user.email,
                        }
                )
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Thank you for your query"
                             "we will be in touch soon!")
            return redirect('home')
    context = {'contact_form': contact_form,
               }

    return render(request, 'contact.html', context)
