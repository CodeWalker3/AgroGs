from django.urls import path
from .views import Home, UserVendorUpdateView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('user_change_form/<int:pk>/', UserVendorUpdateView.as_view(), name="user-update" )
]
