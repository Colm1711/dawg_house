# Imports

# Django imports
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Internal imports
from .forms import UpdateUserForm, UpdateUserProfileForm, ServiceProviderForm


@login_required
def update_profile(request):
    """
    This function handles rendering of the update page to the user
    and logic to update.
    User must be signed in to do this.
    """
    template = 'profiles/profile.html'
    success_message = "Success"
    error_message = "Fail"
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
            return redirect('profile')
        else:
            # send message to user if something goes wrong and redirect
            print(error_message)
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
    user = User.objects.filter(id=request.user.id)
    user.delete()
    return HttpResponseRedirect('/')


@login_required
def serviceprovider(request, id=id):
    """
    This form is for Service Provider to fill out their details.
    """
    form = ServiceProviderForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/')
    else:
        form = ServiceProviderForm()
    return render(request, "profiles/serviceprovider.html", {"form": form})
