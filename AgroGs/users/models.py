from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_vendor = models.BooleanField(
        default=False
    )
    cnpj = models.CharField(
        verbose_name="CNPJ",
        max_length=100,
        null=True, blank=True
    )
    profile_pic = models.ImageField(
        verbose_name="Profile Picture",
        null = True, blank=True,
        upload_to="AgroGs/media/users",
        
    )
    class Meta:
        app_label="users"
        verbose_name='User'
        verbose_name_plural='Users'
        

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
    
    class Meta:
        app_label="users"
        verbose_name='Address'
        verbose_name_plural='Addresses'
    