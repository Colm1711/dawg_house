from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_profile, name='profile'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('serviceprovider/', views.serviceprovider, name='serviceprovider'),
    path('myservices/', views.update_serviceprovider, name='myservices'),
]
