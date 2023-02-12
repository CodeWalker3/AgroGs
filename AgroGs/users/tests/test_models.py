from AgroGs.users.tests.test_base import UserFactory
from AgroGs.users.models import UserProfile
from django.test import TestCase

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()


    def test_profile_str(self):
        profile= UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)
