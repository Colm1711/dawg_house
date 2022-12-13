# Imports

# Djanog Imports
from django.urls import path

# Internal
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<service_id>/', views.add_to_bag, name='add_to_bag'),
]
