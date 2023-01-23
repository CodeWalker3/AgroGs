from django.db import models
from django.db.models import F, Sum
from AgroGs.users.models import User
from AgroGs.products.models import Products
# Create your models here.

class Cart(models.Model):
    total = models.DecimalField(
        verbose_name="Total",
        max_digits=25, decimal_places=2,
        blank=True, null=True
    )
    user = models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products, 
        verbose_name="Product",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    class Meta:
        app_label='cart'
        verbose_name='Cart'
        verbose_name_plural='Cart'

