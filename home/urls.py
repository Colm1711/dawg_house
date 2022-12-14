# Imports

# Djanog Imports
from django.contrib import admin
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
]
