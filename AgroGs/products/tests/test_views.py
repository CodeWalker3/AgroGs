from django.test import RequestFactory, TestCase
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from factory import Faker
from django.contrib.auth.models import Group
from AgroGs.products.models import Products, Category
from AgroGs.products.views import ProductsList, ProductsUserMixin, DeleteProduct, UpdateProduct, CreateProduct
from AgroGs.products.tests.test_base import ProductFactory, CategoryFactory
from AgroGs.users.tests.test_base import UserFactory
from AgroGs.users.models import User
from factory.django import ImageField
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
        
class DeleteProductTestCase(TestCase):
    def setUp(self):
        self.vendor_group, created = Group.objects.get_or_create(name='vendor')
        self.factory = RequestFactory()
        self.user = UserFactory()
        self.user.groups.add(self.vendor_group)
        self.product = ProductFactory()
        

    def test_delete_product_get(self):
        request = self.factory.get(reverse_lazy('products:delete', args=[self.product.pk]))
        request.user = self.user
        response = DeleteProduct.as_view()(request, pk=self.product.pk)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Products.objects.filter(pk=self.product.pk).exists())
    


class UpdateProductTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.vendor = UserFactory()
        self.product = ProductFactory(created_by=self.vendor)
        self.url = reverse_lazy('products:update', args=(self.product.id,))
    
    def test_update_product_initial_data(self):
        request = self.factory.get(self.url)
        request.user = self.vendor
        response = UpdateProduct.as_view()(request, pk=self.product.id)

        self.assertEqual(response.context_data['form'].initial['created_by'], self.vendor)

class CreateProductTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.vendor_group, created = Group.objects.get_or_create(name='vendor')
        self.user = UserFactory()
        self.vendor = UserFactory()
        self.category = CategoryFactory()
        self.vendor.groups.add(self.vendor_group)

    def test_create_product_initial_data(self):
        request = self.factory.get(reverse_lazy('products:create'))
        request.user = self.vendor
        response = CreateProduct.as_view()(request)
        self.assertEqual(response.context_data['form'].initial['created_by'], self.vendor)

    def test_create_product_form_valid(self):
        request = self.factory.post(reverse_lazy('products:create'), data={
        'name': 'Product Test', 
        'created_by': self.vendor,
        'category': self.category.pk,
        'price':12.2,
        'description':'lalalala'
        })
        request.user = self.vendor
        response = CreateProduct.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Products.objects.last().name, 'Product Test')