from django.test import RequestFactory, TestCase
from django.shortcuts import redirect
from django.urls import reverse_lazy
from factory import Faker
from django.contrib.auth.models import Group
from AgroGs.products.models import Products, Category
from AgroGs.products.views import ProductsList, ProductsUserMixin
from AgroGs.products.tests.test_base import ProductFactory, CategoryFactory
from AgroGs.users.tests.test_base import UserFactory
from AgroGs.users.models import User

class ProductsListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory()
        self.products = ProductFactory.create_batch(5, created_by=self.user)

    def test_products_list_view(self):
        request = self.factory.get('/products/')
        request.user = self.user
        response = ProductsList.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 5)

class ProductsUserMixinTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.vendor_group, created = Group.objects.get_or_create(name='vendor')
        self.user = UserFactory()
        self.vendor = UserFactory()
        self.vendor.groups.add(self.vendor_group)
        self.product = ProductFactory(created_by=self.vendor)
    
    def test_handle_no_permission_redirects_to_shop(self):
        request = self.factory.get('/')
        request.user = self.user

        mixin = ProductsUserMixin()
        mixin.request = request
        response = mixin.handle_no_permission()

        self.assertEqual(response.url, reverse_lazy('shop'))

    def test_test_func_returns_true_for_vendor(self):
        request = self.factory.get('/')
        request.user = self.vendor

        mixin = ProductsUserMixin()
        mixin.request = request
        self.assertTrue(mixin.test_func())

    def test_test_func_returns_false_for_non_vendor(self):
        request = self.factory.get('/')
        request.user = self.user

        mixin = ProductsUserMixin()
        mixin.request = request
        self.assertFalse(mixin.test_func())