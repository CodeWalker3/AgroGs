from django.urls import path
from .views import (
    ProductsList, 
    CreateProduct,
    UpdateProduct, 
    UpdateCategory
)
app_name = "products"
urlpatterns = [
    path('list', ProductsList.as_view(), name='list'),
    path('create', CreateProduct.as_view(), name='create'),
 
]
