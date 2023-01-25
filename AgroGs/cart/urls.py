from django.urls import path
from .views import (
    CartView,
    cart_add
    
    )
urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add_item/<int:pk>', cart_add, name='add_item'),
]
