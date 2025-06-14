from django import path
from .import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    
]
