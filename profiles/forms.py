# Imports

# All auth imports
from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm

# Django imports
from django import forms
from django.contrib.auth.models import User

# Internal imports
from .models import UserProfile, ServiceProvider


class RegisterForm(SignupForm):
    """
    Form to Customize Registration to include additonal
    User fields.

    This form overrides the django-allauth registration form.
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
        user.userprofile.first_name = self.cleaned_data['first_name']
        user.userprofile.last_name = self.cleaned_data['last_name']
        user.userprofile.phone_number = self.cleaned_data['phone_number']
        user.userprofile.is_service_provider = self.cleaned_data[
                                                    'is_service_provider']
        user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    """
    Class controls form for updating User details to User Model
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']


class UpdateUserProfileForm(forms.ModelForm):
    """
    Class controls form for updating User details to User Profile Model
    """
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number']


class ServiceProviderForm(forms.ModelForm):
    """
    Class controls form for Service provider details to
    Service Provider Model
    """
    class Meta:
        model = ServiceProvider
        exclude = ("user", "slug", "created_on", "updated_on", "longitude",
                   "latitude",)
