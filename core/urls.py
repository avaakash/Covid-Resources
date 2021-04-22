from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-resource', views.add_resource, name='add_resource'),
    path('add-request', views.request_resource, name='request_resources'),
]
