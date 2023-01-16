from django.db import models
from AgroGs.products.models import Products
from django.contrib.auth.models import User
# Create your models here.

class PaymentMethod(models.Model):
    name = models.CharField(
        max_length=100,
        null=False, blank=False,
    )
    def __str__(self):
        return self.name
class Orders(models.Model):
    ChoiceStatus = (
        ('', ''),
        ('', '')
    )
    total = models.DecimalField(
        verbose_name="Total",
        max_digits=25, decimal_places=2,
        blank=2, null=False
    )
    status = models.CharField(
        ChoiceStatus,
        max_length=100
        )
    order_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    product = models.ManyToManyField(
        Products,
        verbose_name="Product",
        )
    client = models.ForeignKey(
        User,
        verbose_name="Client",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        )
    payment = models.ForeignKey(
        PaymentMethod,
        verbose_name="Payment",
        null=True, blank=False,
        on_delete=models.SET_NULL
        )