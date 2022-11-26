from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateUserProfileForm


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
