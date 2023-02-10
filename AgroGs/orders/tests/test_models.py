from django.test import TestCase

from AgroGs.orders.models import Orders
from .test_base import PaymentMethodFactory, OrdersFactory

class OrdersTestCase(TestCase):
    def setUp(self):
        self.order = OrdersFactory()
        self.payment = PaymentMethodFactory()

    def test_orders_creation(self):
        self.assertEqual(Orders.objects.count(), 1)
        self.assertEqual(self.order.total, self.order.total)
        self.assertEqual(self.order.order_date, self.order.order_date)
        self.assertEqual(self.order.update_date, self.order.update_date)
        self.assertEqual(self.order.user, self.order.user)
        self.assertEqual(self.order.payment, self.order.payment)
    
    def test_str_representation(self):
        self.assertEqual(str(self.payment), self.payment.name)