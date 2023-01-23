# Imports

# Django imports
from django import forms
# Internal imports
from .models import Service, Comment


class ServiceForm(forms.ModelForm):
    """Return Form to Super User to add/edit Service"""
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('slug',)


class ReviewForm(forms.ModelForm):
    """Return Form to add a Service"""
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('service', 'created_on', 'is_approved',)
