from django.contrib import admin
from django.urls import path, include
from .views import (
    OrdersListView,
    OrdersCreateView
)


app_name = "orders"

urlpatterns = [
    path('list/', OrdersListView.as_view(), name="list"),
    path('create/', OrdersCreateView.as_view(), name="create")
    ]