from django.test import TestCase
from AgroGs.products.models import Products
from AgroGs.products.tests.test_base import ProductFactory, CategoryFactory


class ProductsTestCase(TestCase):
    def setUp(self):
        self.product = ProductFactory()
        self.category = CategoryFactory()
    def test_product_creation(self):
        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(self.product.name, self.product.name)
        self.assertEqual(self.product.price, self.product.price)
        self.assertEqual(self.product.description, self.product.description)
        self.assertEqual(self.product.category, self.product.category)
        self.assertEqual(self.product.created_by, self.product.created_by)

    def test_str_representation(self):
        self.assertEqual(str(self.category), self.category.name)
    
    def test_str_representation(self):
        self.assertEqual(str(self.product), self.product.name)
    def test_category_str(self):
        self.assertEquals(str(self.category), self.category.name)