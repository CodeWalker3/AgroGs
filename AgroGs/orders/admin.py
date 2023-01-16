from django.contrib import admin
from .models import Orders, PaymentMethod
# Register your models here.
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'total',
        'order_date',
        'update_date',
    ]

    search_fields = [
        'id',
    ]