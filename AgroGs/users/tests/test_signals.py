from AgroGs.users.models import User, UserProfile
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from django.test import TestCase, Client
from AgroGs.users.tests.test_base import UserFactory

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_create_profile(self):
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())
