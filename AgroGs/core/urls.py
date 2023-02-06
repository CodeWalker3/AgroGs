from django.urls import path, include
from AgroGs.core.views import (
    HomeView,
    ShopView,
    ProductDetailView,
    CheckoutView
)

from AgroGs.products.urls import products_router

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('shop', ShopView.as_view(), name="shop"),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('checkout', CheckoutView.as_view(), name="checkout"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/products/', include(products_router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
] 