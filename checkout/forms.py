# Imports

# Django imports
from django import forms

# Internal imports
from .models import ServiceOrder


class ServiceOderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = (
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                    'address_1',
                    'address_2',
                    'county',
                    'eircode',
                )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address_1': 'Address 1',
            'address_2': 'Address 2',
            'county': 'County',
            'eircode': 'Eir Code',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
