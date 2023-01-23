# Imports

# Django imports
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('review/<slug:slug>', views.service_comments, name='review_service'),
    path('deletereview/<int:id>', views.delete_review, name='delete_review'),
    path('addreview/<slug:slug>', views.add_review, name='add_review'),
    path('add/', views.add_service, name='add_service'),
    path('edit/<slug:slug>', views.edit_service, name='edit_service'),
    path('delete/<int:id>', views.delete_service, name='delete_service'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]
