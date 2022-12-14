# Imports

# Django Imports
from django.contrib import admin
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
]