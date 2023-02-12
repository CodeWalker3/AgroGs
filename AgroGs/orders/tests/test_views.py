from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from AgroGs.orders.views import OrdersCreateView, OrdersListView
from AgroGs.products.tests.test_base import ProductFactory
from AgroGs.users.models import Address, User
from AgroGs.products.models import Products
from AgroGs.orders.models import Orders, ProductOrder
from AgroGs.orders.tests.test_base import OrdersFactory, ProductOrderFactory
from AgroGs.users.tests.test_base import UserFactory
from django.contrib.sessions.backends.db import SessionStore
from cart.cart import Cart

class OrdersListViewTestCase(TestCase):

    def setUp(self):
        # Create a user to test with
        self.user = UserFactory()
        self.factory = RequestFactory()
        # Create a product to test with
        self.product = ProductFactory()

        # Create an order and a product order through the factories
        self.order = OrdersFactory(user=self.user)
        self.product_order = ProductOrderFactory(
            product=self.product,
            order=self.order,
            quantity=2
        )

        # Create a client to test with
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    # def test_orders_list_view(self):
    #     # Get the response from the view
    #     response = self.client.get('/orders/list/')

    #     # Check that the response has a status code of 200 (success)
    #     self.assertEqual(response.status_code, 302)

    #     # Check that the correct object is passed to the context
    #     if response.context['object_list'] is not None:
    #         self.assertEqual(response.context['object_list'][0], self.order)
    #     else:
    #         self.fail("The object_list in the response context is None")

    #     # Check that the correct form is passed to the context
    #     self.assertIsNotNone(response.context['form_filter'])

    #     # Check that the correct template is used
    #     self.assertTemplateUsed(response, 'orders/orders_list.html')

    def test_get_queryset(self):
        # Get an instance of the view
        view = OrdersListView()

        # Create a request object to pass to the view
        request = RequestFactory().get('/orders/list/')
        request.user = self.user

        # Set the request on the view
        view.request = request

        # Get the queryset from the view
        queryset = view.get_queryset()

        # Check that the queryset only contains the order created for this user
        self.assertEqual(len(queryset), 1)
        self.assertEqual(queryset[0], self.order)
    
    def test_get_context_data(self):
        # Get an instance of the view
        request = self.factory.get(reverse_lazy('orders:list'))
        request.user = self.user
        response = OrdersListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)
        

class OrdersCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="email@email.com",
            password="teste"
        )
        self.product = ProductFactory()
        self.view = OrdersCreateView.as_view()

    def test_get_request_with_existing_address(self):
        Address.objects.create(
            city='Test City',
            state='Test State',
            phone='1234567890',
            street='Test Street',
            number=123,
            compliment='Test Compliment',
            user=self.user
        )
        self.client.login(username="teste", password="teste")
        response = self.client.get(reverse('orders:create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/checkout.html')

    def test_get_request_without_existing_address(self):
        self.client.login(username="teste", password="teste")
        response = self.client.get(reverse('orders:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/checkout.html')
        self.assertContains(response, 'form')

    def test_post_request_with_existing_address(self):
        Address.objects.create(
            city='Test City',
            state='Test State',
            phone='1234567890',
            street='Test Street',
            number=123,
            compliment='Test Compliment',
            user=self.user
        )
        self.client.login(username="teste", password="teste")
        session = self.client.session
        session['cart'] = {str(self.product.id): {'product_id': self.product.id, 'quantity': self.product.quantity , 'price':float(self.product.price)},}
        session.save()
        response = self.client.post(reverse('orders:create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Orders.objects.count(), 1)
        self.assertEqual(ProductOrder.objects.count(), 1)
        self.assertEqual(ProductOrder.objects.first().product, self.product)
        self.assertEqual(ProductOrder.objects.first().quantity, self.product.quantity)
    
    def test_post_request_with_new_address(self):
        self.client.login(username="teste", password="teste")
        session = self.client.session
        session['cart'] = {str(self.product.id): {'product_id': self.product.id, 'quantity': self.product.quantity , 'price':float(self.product.price)},}
        session.save()

        data = {
            'city': 'Test City',
            'state': 'Test State',
            'phone': '1234567890',
            'street': 'Test Street',
            'number': 123,
            'compliment': 'Test Compliment'
        }

        response = self.client.post(reverse('orders:create'), data)
        self.assertEqual(response.status_code, 302)




