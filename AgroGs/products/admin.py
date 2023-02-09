from django.contrib import admin

# Register your models here.
from .models import (
    Category, 
    Products
)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'name',
        'price'
    ]

