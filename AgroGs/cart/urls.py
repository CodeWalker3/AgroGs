from django.urls import path
from .views import (
    CartView, 
    
    )
urlpatterns = [
    path('/cart_test', CartView.as_view(), name='cart_test'),
 
]
