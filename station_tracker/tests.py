from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client  # Use Django's test client

class MyTestCase(TestCase):

    def test_user_signup_view(self):
        client = Client()  # Create a test client
        response = client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_user_login_view(self):
        client = Client()  # Create a test client
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_logout_view(self):
         client = Client()  # Create a test client
         response = client.get(reverse('logout'))
         self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
         self.assertFalse(response.context['user'].is_authenticated)

