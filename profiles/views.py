from django.shortcuts import render


def update_profile(request):
    """
    This function handles rendering of the update page to the user
    and logic to update.
    User must be signed in to do this.
    """
    template = 'profiles/profile.html'
    return render(request, template)
