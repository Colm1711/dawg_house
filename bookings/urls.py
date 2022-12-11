from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_service_providers, name='booking'),
    path('serviceproviders/', views.list_service_providers,
         name='serviceproviderslist'),
    path('bookingform/<int:pk>', views.booking_form, name='bookingform'),
]
