from django.db import models
from AgroGs.users.models import User
from AgroGs.products.models import Products
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="User",
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        verbose_name="Total Sum of cart",
        max_digits=7, 
        decimal_places=2, 
        default=0
    )

    def __str__(self):
        return self.user.username
    class Meta:
        app_label='cart'
        verbose_name='Cart'
        verbose_name_plural='Cart'

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="Cart",
        null=True,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products,
        verbose_name="Product",
        null=True,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1
    )
    total = models.DecimalField(
        verbose_name="Total Sum",
        max_digits=7, 
        decimal_places=2, 
        default=0
    )
    def __str__(self):
        return self.product.name

    def get_total(self):
        return round(float(self.product.price) * float(self.quantity))

    def save(self, *args, **kwargs):
        self.total = self.get_total()
        super().save(*args, **kwargs)