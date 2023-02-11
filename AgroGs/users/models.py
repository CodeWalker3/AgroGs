from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_vendor = models.BooleanField(
        default=False
    )
    cnpj = models.CharField(
        verbose_name="Cnpj",
        max_length=100,
        null=True, blank=True
    )
    class Meta:
        app_label="users"
        verbose_name='User'
        verbose_name_plural='Users'

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        primary_key=True, 
        verbose_name='user', 
        related_name='profile',
        on_delete=models.CASCADE    
    )
    pic = models.ImageField(
        verbose_name="Profile Picture",
        default="default.jpg",
        upload_to="profile_images",
    )
    def __str__(self):
        return self.user.username_validator
class Address(models.Model):
    city = models.CharField(
        verbose_name="City",
        max_length=100,
        null=False, blank=False
    )
    state = models.CharField(
        verbose_name="State",
        max_length=100,
        null=False, blank=False
    )
    phone = models.CharField(
        verbose_name="Phone",
        max_length=100,
        null=False, blank=False
    )
    street = models.CharField(
        verbose_name="Street",
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
    