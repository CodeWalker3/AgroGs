from django.test import Client, RequestFactory, TestCase
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from factory import Faker
from django.contrib.auth.models import Group
from AgroGs.users.tests.test_base import UserFactory
from AgroGs.users.models import User, UserProfile
from AgroGs.users.views import profile, UserVendorUpdateView
from factory.django import ImageField
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase

from AgroGs.users.forms import ProfileUpdateForm

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = self.user.profile
        self.client.login(username='testuser', password='password')

    def test_profile_view_get(self):
        response = self.client.get(reverse('users:test'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('p_form', response.context)
        self.assertEqual(response.context['p_form'].instance, self.user_profile.user)

    def test_profile_view_post(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('users:test'), data={
            'image': image,
        })
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your Profile has been updated!')

class UserVendorUpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.vendor_group, created = Group.objects.get_or_create(name='vendor')
        self.factory = RequestFactory()
        self.user = UserFactory()
        self.url = reverse_lazy('users:user-update', args=(self.user.id,))

    def test_get_initial(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = UserVendorUpdateView.as_view()(request, pk=self.user.id)
        self.assertEqual(response.context_data['form'].initial['is_vendor'], True)

    def test_get_object(self):
        request = self.factory.get(self.url)
        request.user = self.user
        view = UserVendorUpdateView()
        view.request = request
        user = view.get_object()
        self.assertEqual(user, self.user)


