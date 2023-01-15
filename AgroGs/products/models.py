from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50
    )
    def __str__(self):
        return self.name




class Products(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        blank=False, null=False
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=20, decimal_places=2,
        blank=False, null=False
    )
    description = models.TextField(
        verbose_name="Description",
        blank=False, null=False
    )
    category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name="Created_By"
	)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label='products'
        verbose_name='Product'
        verbose_name_plural='Products'
        ordering = ['name']

