from django.urls import path
from .views import (
    CartView,
    cart_add,
    remove_item
    
    )
urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add_item/<int:pk>', cart_add, name='add_item'),
    path('remove_item/<int:pk>', remove_item, name='remove_item')
]
