from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(SignupForm):
    """
    Form to Customize Registration to include additonal
    User fields.
    """

    # Setting the custom profile fields to add to form
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput
                                 (
                                  attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput
                                (
                                  attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(max_length=20,
                                   widget=forms.TextInput
                                   (
                                    attrs={'placeholder': 'Phone Number'}))
    is_service_provider = forms.BooleanField(required=False)

    # Overriding the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
        }
        # Remove username as will not be used
        del self.fields["username"]
        # Set email as the autofocus
        self.fields["email"].widget.attrs["autofocus"] = True
        self.fields['phone_number'].widget.attrs['type'] = "number"

    # saving the user data from form to User and UserProfile
    def save(self, request):
        # .save() returns a User object.
        user = super(RegisterForm, self).save(request)
        return user
