from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, UserVendorUpdateView, profile, test_user_profile
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('user_change_form/<int:pk>/', UserVendorUpdateView.as_view(), name="user-update" ),
    path('test', profile ,name='test'),
    path('test1', test_user_profile,name='test1')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
