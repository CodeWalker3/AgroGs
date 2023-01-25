from django.test import TestCase, Client
from AgroGs.cart.models import Cart, CartItem
from AgroGs.users.tests.test_base import TestBaseUser
from AgroGs.products.tests.test_base import TestBaseProducts
class TestBaseCart(TestCase):
    def create_cart(self):
        user = TestBaseUser.create_user
        cart = Cart(
            user=user
        )
        return cart
    def create_cart_item(self):
        cart = self.create_cart()
        product = TestBaseProducts.create_product()
        cart_item = CartItem(
        cart = cart,
        product = product,
        quantity = 1
        )
        return cart_item