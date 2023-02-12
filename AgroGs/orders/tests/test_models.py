from django.test import TestCase

from AgroGs.orders.models import Orders
from .test_base import OrdersFactory

class OrdersTestCase(TestCase):
    def setUp(self):
        self.order = OrdersFactory()
    

    def test_orders_creation(self):
        self.assertEqual(Orders.objects.count(), 1)
        self.assertEqual(self.order.total, self.order.total)
        self.assertEqual(self.order.order_date, self.order.order_date)
        self.assertEqual(self.order.update_date, self.order.update_date)
        self.assertEqual(self.order.user, self.order.user)
    def test_str_order(self):
        self.assertEqual(str(self.order), str(self.order.id))
