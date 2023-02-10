from django.test import TestCase, Client
from AgroGs.users.models import User
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory

class UserFactory(DjangoModelFactory):
    username =  Faker("name")
    email = Faker("email")
    password = "Teste"
    class Meta:
        model = User
        django_get_or_create = ['username']
        django_get_or_create = ['email']

