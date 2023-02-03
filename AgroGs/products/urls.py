from django.urls import path, include
from rest_framework import routers

from .views import (
    ProductsList, 
    CreateProduct,
    UpdateProduct, 
    UpdateCategory,
    DeleteProduct
)
from AgroGs.products.api.viewsets import ProductsViewSet

app_name = "products"

products_router = routers.DefaultRouter()
products_router.register('', ProductsViewSet, basename="products")

urlpatterns = [
    path('list', ProductsList.as_view(), name='list'),
    path('create', CreateProduct.as_view(), name='create'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete'),
 
]
