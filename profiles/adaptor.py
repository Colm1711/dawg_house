from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url


class AccountAdapter(DefaultAccountAdapter):
    """
    This class handles the log in rediect for when user is
    a service provider or just a general user.

    User redirected to settings.LOGIN_REDIRECT_URL = Home

    Sends service provider to 'serviceprovider' for DEVELOPMENT will update
    this.
    """
    def get_login_redirect_url(self, request):

        if request.user.userprofile.is_service_provider is True:
            url = 'serviceprovider'
        else:
            url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)
