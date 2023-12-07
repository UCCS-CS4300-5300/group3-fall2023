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

#himaja test cases
class MyTestCase(TestCase):

    def test_user_signup_view(self):
        client = Client()  # Create a test client
        response = client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


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


class ViewsTestCase(TestCase):
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

class ModelTest(TestCase):

  def setUp(self):
      self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
      self.about_us = AboutUs.objects.create(
          title="Title",
          content="Content",
          image=self.image
      )
  
  def test_about_us_model(self):
      about_us_from_db = AboutUs.objects.get(id=self.about_us.id)
  
      self.assertEqual(about_us_from_db.title, "Title")
      self.assertEqual(about_us_from_db.content, "Content")
      self.assertNotEqual(about_us_from_db.image, "about_us_images/test_image.jpg")
  
  

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, GasStationOwner, Gas_Station, Feedback

class YourAppTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get('/index/')  # Replace '/index/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_main_view_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get('/main/')  # Replace '/main/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_user_signup_view(self):
        response = self.client.get('/signup/')  # Replace '/signup/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_user_login_view(self):
        response = self.client.get('/login/')  # Replace '/login/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_logout_view(self):
        response = self.client.get('/logout/')  # Replace '/logout/' with your actual URL
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout

    def test_update_gas_prices_view(self):
        self.client.force_login(self.user)
        response = self.client.get('/update_gas_prices/')  # Replace '/update_gas_prices/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_gas_prices.html')

    def test_render_feedback_form_view(self):
        response = self.client.get('/feedback/')  # Replace '/feedback/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

    def test_map_view(self):
        response = self.client.get('/map/')  # Replace '/map/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'station-tracker.html')

    def test_user_about_view(self):
        response = self.client.get('/about/')  # Replace '/about/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_user_fueldemand_view(self):
        response = self.client.get('/fueldemand/')  # Replace '/fueldemand/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fueldemand.html')

    def test_user_stationowner_view(self):
        response = self.client.get('/stationowner/')  # Replace '/stationowner/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stationowner.html')

    def test_user_payment_view(self):
        response = self.client.get('/payment/')  # Replace '/payment/' with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment.html')

    # Add more test cases as needed
