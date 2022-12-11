from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_service_providers, name='booking'),
    path('serviceproviders/', views.list_service_providers,
         name='serviceproviderslist'),
    path('bookingform/', views.booking_form, name='bookingform'),
]
