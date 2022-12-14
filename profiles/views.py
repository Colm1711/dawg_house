# Imports

# Django imports
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Internal imports
from .forms import UpdateUserForm, UpdateUserProfileForm, ServiceProviderForm
from .models import ServiceProvider
from .decorators import service_provider_required


@login_required
def update_profile(request):
    """
    This function handles rendering of the update page to the user
    and logic to update.
    User must be signed in to do this.
    """
    template = 'profiles/profile.html'
    success_message = 'Profile updated successfully'
    error_message = 'Update failed. Please ensure the form is valid.'
    userprofile = request.user.userprofile

    if request.method == 'POST':
        # post forms
        user_update_form = UpdateUserForm(request.POST, instance=request.user)
        profile_update_form = UpdateUserProfileForm(request.POST,
                                                    instance=userprofile)

        # save new user data if forms are valid
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, success_message)
            return redirect('profile')
        else:
            # send message to user if something goes wrong
            messages.error(request, error_message)
    else:
        # get forms to show current data to user
        user_update_form = UpdateUserForm(instance=request.user)
        profile_update_form = UpdateUserProfileForm(
                                                    instance=userprofile)

        # pass forms to the html form
        context = {
                    'user_update_form': user_update_form,
                    'profile_update_form': profile_update_form,
                    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    Function to handle user account deletion on my account page.
    Redirects user back to the home screen post deletion.
    """
    error_message = ("Successfully Deleted profile. We are sad to see"
                     " you go!")
    user = User.objects.filter(id=request.user.id)
    messages.error(request, error_message)
    user.delete()
    return HttpResponseRedirect('/')


@service_provider_required
@login_required
def serviceprovider(request):
    """
    This form is for Service Provider to fill out their details.

    Function will check to see if user exists via try/except.

    If True will render home page.

    If false will render the form to add details for first time.

    """
    success_message = 'Your Services Profile has been added successfully'
    # checking to see if user already has instance of serviceprovider instance
    try:
        testuser = request.user.userprofile.serviceprovider
        serviceprovider = ServiceProvider.objects.get(id=testuser.id)
        if ServiceProvider.objects.filter(id=serviceprovider.id).exists():
            return redirect('/')
    # if user doesn't exists present user with form to fill out details
    except ServiceProvider.DoesNotExist:
        form = ServiceProviderForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user.userprofile
            form.save()
            messages.success(request, success_message)
            return redirect('/')
        return render(request, "profiles/serviceprovider.html", {"form": form})


@service_provider_required
@login_required
def update_serviceprovider(request, *args, **kwargs):
    """
    This form is for Service Provider to update their services details.
    """
    success_message = 'Your Services Profile updated successfully'
    # add try block in case new user tries to access my services profile before
    # adding details
    try:
        if request.method == 'POST':
            form = ServiceProviderForm(request.POST,
                                       instance=request.user.userprofile.
                                       serviceprovider)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                messages.success(request, success_message)
                return redirect('/')

        else:
            form = ServiceProviderForm(instance=request.user.userprofile.
                                       serviceprovider)

        context = {
                    'form': form
                    }

        return render(request, "profiles/myservices.html", context)
    except ServiceProvider.DoesNotExist:
        return redirect('serviceprovider')
