# Imports
import functools

# Django imports
from django.shortcuts import redirect
from django.contrib import messages


def service_provider_required(view_func, redirect_url="home"):
    """
    This decorator ensures that a user has to be a serviceprovider
    to access this url.
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.userprofile.is_service_provider is True:
            return view_func(request, *args, **kwargs)
        messages.info(request, "You need to sign up to be a service provider"
                      " to access this page")
        return redirect(redirect_url)
    return wrapper
