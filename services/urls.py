# Imports

# Django imports
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('add/', views.add_service, name='add_service'),
    path('edit/<slug:slug>', views.edit_service, name='edit_service'),
    path('delete/<slug>', views.delete_service, name='delete_service'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]
