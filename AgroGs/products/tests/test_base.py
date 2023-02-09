from django.test import TestCase
from AgroGs.products.models import Products, Category
from AgroGs.users.tests.test_base import TestBaseUser
from AgroGs.users.models import User
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory


from factory.fuzzy import FuzzyInteger, FuzzyDecimal

class UserFactory(DjangoModelFactory):

    username =  Faker("name")
    email = Faker("email")
    password = Faker("password")
    class Meta:
        models = User
        django_get_or_create = ['username']
        django_get_or_create = ['email']

class ProductFactory(DjangoModelFactory):

    name = Faker("name")
    quantity = FuzzyInteger(1,200)
    user = SubFactory(UserFactory)

    class Meta:
        models = Products
        django_get_or_create = ["name"]


# class TestBaseProducts(TestCase):
#     def create_category(self):
#         category = Category(
#             name="Verduras"
#         )
#         return category
#     def create_product(self):
#         category = self.create_category()
#         user = TestBaseUser.create_user()
#         product = Products(
#         name = "Feijao",
#         price = 12.2,
#         description = "Feijao preto é o feijao mais comum no sul",
#         category= category,
#         user = user
#         )
#         return product