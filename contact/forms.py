# Imports

# Django imports
from django import forms

# Internal imports
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class for contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('is_replied',)
