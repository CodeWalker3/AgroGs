from django.contrib import admin
from django.urls import path
from AgroGs.core.views import (
    HomeView,
    ShopView,
    ProductDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('shop', ShopView.as_view(), name="shop"),
    path('product-detail<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('shop', ShopView.as_view(), name="shop"),
]