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
    address_1 = forms.CharField(max_length=20,
                                widget=forms.TextInput
                                (
                                 attrs={'placeholder': 'Address 1'}))
    address_2 = forms.CharField(max_length=20, required=False,
                                widget=forms.TextInput
                                (
                                 attrs={'placeholder': 'Address 2'}))
    county = forms.CharField(max_length=20,
                             widget=forms.TextInput
                             (
                              attrs={'placeholder': 'County'}))
    eircode = forms.CharField(max_length=7,
                              widget=forms.TextInput
                              (
                                attrs={'placeholder': 'Eir Code'}))
    is_service_provider = forms.BooleanField(required=False)

    # Overriding the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove username as will not be used
        del self.fields["username"]
        # Set email as the autofocus
        self.fields["email"].widget.attrs["autofocus"] = True

    # saving the user data from form to User and UserProfile
    def save(self, request):
        # .save() returns a User object.
        user = super(RegisterForm, self).save(request)
        user.userprofile.first_name = self.cleaned_data['first_name']
        user.userprofile.last_name = self.cleaned_data['last_name']
        user.userprofile.phone_number = self.cleaned_data['phone_number']
        user.userprofile.address_1 = self.cleaned_data['address_1']
        user.userprofile.address_2 = self.cleaned_data['address_2']
        user.userprofile.county = self.cleaned_data['county']
        user.userprofile.eircode = self.cleaned_data['eircode']
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
    is_service_provider = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'address_1',
                  'address_2', 'county', 'eircode', 'is_service_provider']

    # get previous selected boolean for service provider for profile
    def clean(self):
        cleaned_data = super().clean()
        is_service_provider = cleaned_data.get('is_service_provider')


class ServiceProviderForm(forms.ModelForm):
    """
    Class controls form for Service provider details to
    Service Provider Model
    """
    class Meta:
        model = ServiceProvider
        exclude = ("user", "created_on", "updated_on", "longitude",
                   "latitude",)
