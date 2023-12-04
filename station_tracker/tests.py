# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client  # Use Django's test client
from django.contrib.auth.models import User
from .models import CustomUser, Gas_Station, Feedback, AboutUs, GasStation, GasStationOwner, GasStationListing, GasStationReview, CustomerInquiry,Feedback
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/runner/group3-fall2023-1')  # Add this line
os.environ['DJANGO_SETTINGS_MODULE'] = 'gas_station_tracker.settings'




class TestModels(TestCase):

    def setUp(self):
        # Create test instances for testing models
        self.user = CustomUser.objects.create(username='test_user', email='test@example.com')
        self.owner = GasStationOwner.objects.create(owner_name='Test Owner', contact_number='123456789', email='owner@example.com', business_address='Test Address')
        self.station = GasStation.objects.create(name='Test Station', location='Test Location', owner=self.owner)
        self.listing = GasStationListing.objects.create(station=self.station, station_owner=self.owner)
        self.review = GasStationReview.objects.create(gas_station=self.listing, user_name='Test Reviewer', rating=4, review_text='Test Review')
        self.inquiry = CustomerInquiry.objects.create(gas_station=self.listing, sender_name='Test Sender', sender_email='sender@example.com', message_text='Test Inquiry')

    def test_custom_user_creation(self):
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_gas_station_creation(self):
        self.assertEqual(GasStation.objects.count(), 1)

    def test_gas_station_owner_creation(self):
        self.assertEqual(GasStationOwner.objects.count(), 1)

    def test_gas_station_listing_creation(self):
        self.assertEqual(GasStationListing.objects.count(), 1)

    def test_gas_station_review_creation(self):
        self.assertEqual(GasStationReview.objects.count(), 1)

    def test_customer_inquiry_creation(self):
        self.assertEqual(CustomerInquiry.objects.count(), 1)




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
    response = client.post(
        reverse('feedback'), {
            'name': 'test',
            'email': 'tzirw@example.com',
            'phone': '1234567890',
            'comments': 'test comments',
            'gasStationAddr': '123 AnyPlace'
        })
    self.assertEqual(response.status_code, 302)

  def test_missing_name(self):
    client = Client()
    response = client.post(
        reverse('feedback'), {
            'email': 'tzirw@example.com',
            'phone': '1234567890',
            'comments': 'test comments',
            'gasStationAddr': '123 AnyPlace'
        })
    self.assertFormError(response, 'form', 'name', 'This field is required.')













