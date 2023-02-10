from django.db import models
from AgroGs.users.models import User

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
    user = models.ManyToManyField(
        User,
        verbose_name="User",
        )
    payment = models.ForeignKey(
        PaymentMethod,
        verbose_name="Payment",
        null=True, blank=False,
        on_delete=models.SET_NULL
        )

