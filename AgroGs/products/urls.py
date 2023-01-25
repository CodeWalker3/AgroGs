from django.urls import path
from .views import (
    ProductsList, 
    CreateProduct,
    UpdateProduct, 
    UpdateCategory
)
urlpatterns = [
    path('products', ProductsList.as_view(), name='products-list'),
    path('new_product', CreateProduct.as_view(), name='new-product'),
 
]
