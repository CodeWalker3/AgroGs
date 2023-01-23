from django.db import models
from AgroGs.orders.models import Orders
from django.db.models import F, Sum
from AgroGs.users.models import User
# Create your models here.

class Cart(models.Model):
    total = models.DecimalField(
        verbose_name="Total",
        max_digits=25, decimal_places=2,
        blank=True, null=True
    )
    orders = models.OneToOneField(
        Orders,
        verbose_name="Order",
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    user = models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.CASCADE
    )
    class Meta:
        app_label='cart'
        verbose_name='Cart'
        verbose_name_plural='Cart'

