# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client  # Use Django's test client
from .models import Feedback

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/runner/group3-fall2023-1')  # Add this line
os.environ['DJANGO_SETTINGS_MODULE'] = 'station_tracker.settings'



class MyTestCase(TestCase):

    def test_user_signup_view(self):
        client = Client()  # Create a test client
        response = client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_user_login_view(self):
        client = Client()  # Create a test client
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

   # def test_user_logout_view(self):
      #   client = Client()  # Create a test client
       #  response = client.get(reverse('logout'))
        # self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        # self.assertFalse(response.context['user'].is_authenticated)
from django.test import TestCase, Client
from django.urls import reverse

class YourAppViewsTestCase(TestCase):
    def setUp(self):
        # Any setup needed for your tests, if applicable
        pass

    def test_about_view(self):
        client = Client()
        response = client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_fueldemand_view(self):
        client = Client()
        response = client.get(reverse('fueldemand'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fueldemand.html')

    def test_stationowner_view(self):
        client = Client()
        response = client.get(reverse('stationowner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stationowner.html')

    def test_payment_view(self):
        client = Client()
        response = client.get(reverse('payment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment.html')




class FeedbackTestCases(TestCase):

  def test_successful_submit(self):
    client = Client()
    response = client.post(reverse('feedback'), {'name': 'test', 'email': 'tzirw@example.com', 'phone': '1234567890', 'comments': 'test comments', 'gasStationAddr': '123 AnyPlace'})
    self.assertEqual(response.status_code, 302)

  def test_missing_name(self):
    client = Client()
    response = client.post(reverse('feedback'), {'email': 'tzirw@example.com', 'phone': '1234567890', 'comments': 'test comments', 'gasStationAddr': '123 AnyPlace'})
    self.assertFormError(response, 'form', 'name', 'This field is required.')

