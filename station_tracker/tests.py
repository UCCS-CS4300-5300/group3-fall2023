# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client  # Use Django's test client
from .models import Feedback, Gas_Station, AboutUs
from .forms import SignupForm, LoginForm, GasPriceUpdateForm, FeedbackForm
from django.core.files.uploadedfile import SimpleUploadedFile

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/runner/group3-fall2023-1')  # Add this line
os.environ['DJANGO_SETTINGS_MODULE'] = 'station_tracker.settings'



class GasStationModelTest(TestCase):
  def test_gas_station_creation(self):
      gas_station = Gas_Station.objects.create(
          station_name="Gas Station",
          latitude=37.7749,
          longitude=-122.4194,
          regular_gas_price=3.50,
          premium_gas_price=4.00,
          diesel_price=3.80,
      )
      self.assertEqual(str(gas_station), "Gas Station")


class FeedbackModelTest(TestCase):
  def test_feedback_creation(self):
      feedback = Feedback.objects.create(
          name="Johnny Jones",
          email="jonhnny@email.com",
          phone=7195555555,
          comments="Comment",
          gasStationAddr="123 Playground Street",
      )
      self.assertEqual(str(feedback), "Johnny Jones")


class YourAppViewsTestCase(TestCase):
  def setUp(self):
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

  def test_user_signup_view(self):
    client = Client()
    response = client.get(reverse('signup')) 
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'signup.html')
  
  def test_user_login_view(self):
    client = Client()
    response = client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

class ViewsTests(TestCase):
  def setUp(self):
      self.client = Client()

  def test_index_view(self):
      response = self.client.get(reverse('index'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'index.html')

  def test_main_view_authenticated_user(self):
      test_user = User.objects.create_user(username='user', password='password')
      self.client.login(username='user', password='password')

      response = self.client.get(reverse('main'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main.html')

class FormsTests(TestCase):
  def test_signup_form_valid(self):
      data = {
          'username': 'user',
          'password1': 'password123',
          'password2': 'password123',
          'email': 'someguy@email.com',
      }
      form = SignupForm(data)
      self.assertFalse(form.is_valid())

  def test_signup_form_invalid(self):
      data = {}
      form = SignupForm(data)
      self.assertFalse(form.is_valid())

  def test_login_form_valid(self):
      data = {
          'username': 'user',
          'password': 'password123',
      }
      form = LoginForm(data)
      self.assertTrue(form.is_valid())

  def test_login_form_invalid(self):
      data = {}
      form = LoginForm(data)
      self.assertFalse(form.is_valid())

  def test_gas_price_update_form_valid(self):
      data = {
          'regular_gas_price': '8.90',
          'premium_gas_price': '5.99',
          'diesel_price': '1.99',
          'station_name': 'Gas Station',
      }
      form = GasPriceUpdateForm(data)
      self.assertTrue(form.is_valid())

  def test_gas_price_update_form_invalid(self):
      data = {}
      form = GasPriceUpdateForm(data)
      self.assertFalse(form.is_valid())

  def test_feedback_form_valid(self):
      data = {
          'name': 'James Montoya',
          'email': 'this@email.com',
          'phone': '7195555555',
          'comments': 'Comment',
          'gasStationAddr': '123 Playground Street',
      }
      form = FeedbackForm(data)
      self.assertTrue(form.is_valid())

  def test_feedback_form_invalid(self):
      data = {}
      form = FeedbackForm(data)
      self.assertFalse(form.is_valid())



class AboutUsModelTest(TestCase):

  def setUp(self):
      self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
      self.about_us = AboutUs.objects.create(
          title="Test Title",
          content="Test Content",
          image=self.image
      )
  
  def test_about_us_model(self):
      about_us_from_db = AboutUs.objects.get(id=self.about_us.id)
  
      self.assertEqual(about_us_from_db.title, "Test Title")
      self.assertEqual(about_us_from_db.content, "Test Content")
      self.assertNotEqual(about_us_from_db.image, "about_us_images/test_image.jpg")
  
  