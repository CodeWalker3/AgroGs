from django.contrib import admin
from django.urls import path, include
from .views import (
    OrdersList
)
urlpatterns = [
    path('orders', OrdersList.as_view(), name="orders_list")
    ]