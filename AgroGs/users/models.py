from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    city = models.CharField(
        verbose_name="City",
        max_length=100,
        null=False, blank=False
    )
    state = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=False, blank=False
    )
    phone = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=True, blank=True
    )
    street = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=False, blank=False
    )
    number = models.IntegerField(
        verbose_name="Number",
        null=False, blank=False
    )
    compliment = models.CharField(
        verbose_name="Compliment",
        max_length=100,
        null=True, blank=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE   
        )
class Vendor(models.Model):
    
    user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE
	)
    is_vendor = models.BooleanField(
        default=False
    )
    cnpj = models.CharField(
        verbose_name="Vendor",
        max_length=100,
        null=False, blank=False
    )