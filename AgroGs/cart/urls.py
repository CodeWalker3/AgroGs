from django.urls import path
from .views import (
    CartView,
    cart_add
    
    )
urlpatterns = [
    path('cart_test', CartView.as_view(), name='cart_test'),
    path('add_item/<int:pk>', cart_add, name='add_item'),
]
