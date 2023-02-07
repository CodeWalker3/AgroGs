from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('AgroGs.users.urls')),
    path('', include('AgroGs.core.urls')),
    path('products/', include('AgroGs.products.urls')),
    path('orders/', include('AgroGs.orders.urls')),
    path('cart', include('AgroGs.cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
