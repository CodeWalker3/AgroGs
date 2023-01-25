from django.test import TestCase
from AgroGs.orders.models import PaymentMethod, Orders
from AgroGs.users.tests.test_base import TestBaseUser
from AgroGs.cart.tests.test_base import TestBaseCart

class TestBasePaymentMethod(TestCase):
    def create_payment(self):
        payment = PaymentMethod(
            name="Cartao"
        )
        return payment
    def create_order(self):
        payment = self.create_payment()
        user = TestBaseUser.create_user()
        cart = TestBaseCart.create_cart()
        order = Orders(
        total = 23,
        status = 'Cancelado',
        cart = cart,
        payment = payment,
        user = user
        )
        return order