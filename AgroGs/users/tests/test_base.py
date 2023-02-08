from django.test import TestCase, Client
from AgroGs.users.models import User

class TestBaseUser(TestCase):
    def create_user(self):
        user = User(
            username="Teste123",
            password="test123",
            email="teste@teste.com",
        )
        user.save()
        return user