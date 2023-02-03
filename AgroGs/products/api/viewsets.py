from rest_framework import viewsets

from AgroGs.products.models import Products
from AgroGs.products.api.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer