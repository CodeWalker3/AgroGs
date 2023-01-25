from django.test import TestCase
from AgroGs.products.models import Products, Category
from AgroGs.users.tests.test_base import TestBaseUser

class TestBaseProducts(TestCase):
    def create_category(self):
        category = Category(
            name="Verduras"
        )
        return category
    def create_product(self):
        category = self.create_category()
        user = TestBaseUser.create_user()
        product = Products(
        name = "Feijao",
        price = 12.2,
        description = "Feijao preto é o feijao mais comum no sul",
        category= category,
        user = user
        )
        return product