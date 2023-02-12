from AgroGs.orders.views import OrdersListView
from AgroGs.products.tests.test_base import ProductFactory
from AgroGs.users.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import resolve, reverse, reverse_lazy
from AgroGs.core.views import HomeView, ShopView, cart_add

class CartTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password')
        self.product = ProductFactory()

    def test_cart_add_view(self):
        self.client.login(username='testuser', password='password')
        url = reverse('cart_add', kwargs={'id': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    
    def test_cart_clear(self):
        self.client.login(username='testuser', password='password')
        url = reverse('item_clear', kwargs={'id': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    def test_increment_view(self):
        self.client.login(username='testuser', password='password')
        url = reverse('item_increment', kwargs={'id': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    def test_decrement_view(self):
        self.client.login(username='testuser', password='password')
        url = reverse('item_decrement', kwargs={'id': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    def test_cart_clear_view(self):
        self.client.login(username='testuser', password='password')
        url = reverse('cart_clear')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
    def test_cart_detail(self):
        self.client.login(username='testuser', password='password')
        url = reverse('cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_shop_context_data(self):
        request = self.factory.get(reverse_lazy('shop'))
        request.user = self.user
        response = ShopView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)
    def test_get_home_context_data(self):
        request = self.factory.get(reverse_lazy('home'))
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)