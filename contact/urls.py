# Imports

# Django imports
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact'),
]
