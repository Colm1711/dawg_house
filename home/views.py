# Imports

# Django imports
from django.shortcuts import render


def index(request):
    """ A view to return the index page"""
    return render(request, 'home/index.html')


def about(request):
    """A view to show the about page"""
    return render(request, "home/about.html")


def privacypolicy(request):
    """A view to show the privacy policy page"""
    return render(request, "home/privacypolicy.html")


def termsconditions(request):
    """A view to show the terma and conditions page"""
    return render(request, "home/termsconditions.html")
