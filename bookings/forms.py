from django import forms
from django.utils import timezone
from .models import ServiceBooking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = ServiceBooking
        fields = ('service_provider_id', 'start_date', 'end_date')
