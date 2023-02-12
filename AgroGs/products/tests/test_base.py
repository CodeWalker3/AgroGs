from django.test import TestCase
from AgroGs.products.models import Products, Category
from AgroGs.users.tests.test_base import UserFactory
from AgroGs.users.models import User
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory, ImageField


from factory.fuzzy import FuzzyInteger, FuzzyDecimal

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker("word")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Products        
    name = Faker("word")
    price = FuzzyDecimal(1,100)
    description = Faker("text")
    quantity = FuzzyInteger(1,100)
    category = SubFactory(CategoryFactory)
    created_by = SubFactory(UserFactory)
    image = ImageField()