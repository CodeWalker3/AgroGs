from django.urls import path, include
from AgroGs.core.views import (
    HomeView,
    ShopView,
    ProductDetailView,
)

from . import views
from AgroGs.products.urls import products_router

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('shop', ShopView.as_view(), name="shop"),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/products/', include(products_router.urls)),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart_detail,name='cart'),
] 
