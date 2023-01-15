from django.contrib import admin
from django.urls import path
from AgroGs.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home")
]