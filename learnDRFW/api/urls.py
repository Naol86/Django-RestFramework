from django.urls import path

from . import views

urlpatterns = [
  path('', views.api_home, name='api_home'),
  path('name', views.index, name='names'),
]