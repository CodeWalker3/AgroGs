from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    
    user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE
	)
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=False, blank=False
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=200,
        null=False, blank=False
    )
    phone = models.CharField(
        verbose_name="Phone",
        max_length=100,
        null=True, blank=True
    )
    cnpj = models.CharField(
        verbose_name="Vendor",
        max_length=100,
        null=False, blank=False
    )