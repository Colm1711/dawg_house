# Imports

# Djanog Imports
from django.contrib import admin
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
