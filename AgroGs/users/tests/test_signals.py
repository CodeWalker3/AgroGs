from AgroGs.users.models import User, UserProfile
from django.contrib.auth.models import Group
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from django.test import TestCase, Client
from AgroGs.users.tests.test_base import UserFactory

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.group = Group.objects.create(
            name="vendor"
        )
        self.admin = User.objects.create_superuser(
            username="teste",
            email="email@email.com",
            password="teste"
        )
    def test_create_profile(self):
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())
    
    def test_create_group_admin(self):
        self.assertTrue(User.objects.filter(groups__name='vendor', is_staff=True).exists())

