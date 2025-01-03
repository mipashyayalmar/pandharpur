from django.urls import path
from . import views

# App-level (puja/urls.py)
urlpatterns = [
    path('', views.home, name='home'),
]
