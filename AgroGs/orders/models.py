from django.db import models
from AgroGs.products.models import Products
from AgroGs.users.models import User

class Orders(models.Model):
    ChoiceStatus = (
        ('Em andamento', 'Em andamento'),
        ('Cancelado', 'Cancelado'),
        ('Entregue', 'Entregue')
    )
    total = models.DecimalField(
        verbose_name="Total",
        max_digits=25, decimal_places=2,
        blank=True, null=True
    )
    status = models.CharField(
        ChoiceStatus,
        max_length=100,
        default= "Em andamento"
        )
    order_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        Products, 
        through='ProductOrder'
        
    )

    def __str__(self):
        return str(self.id)


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Orders, 
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        blank=False, null=False
    )