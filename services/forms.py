# Imports

# Django imports
from django import forms
# Internal imports
from .models import Service, Breed


class ServiceForm(forms.ModelForm):
    """Return Form to Super User to edit Service"""
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('slug',)
