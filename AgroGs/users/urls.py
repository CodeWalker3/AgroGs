from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, UserVendorUpdateView, profile
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('user_change_form/<int:pk>/', UserVendorUpdateView.as_view(), name="user-update" ),
    path('test', profile ,name='test')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
