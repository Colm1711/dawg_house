from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]
