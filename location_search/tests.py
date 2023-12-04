from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Gas_Station, Search
from django.contrib.auth.models import User
from django.test import RequestFactory

class SearchViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_searchPage_view(self):
        response = self.client.get(reverse('searchPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stuff.html')

    def test_submit_view_post_method(self):
        data = {
            'location': 'Test location',
            'range': 100,
            'gasType': 'Test gas type',
            'preferenceSelect': 'Test preference'
        }
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('submit'), data)
        self.assertEqual(response.status_code, 200)  # Assuming successful submission leads to a 200 status code

        # Add assertions for checking database entries after submission

    @patch('geopy.geocoders.Nominatim.geocode')
    def test_map_view(self, mock_geocode):
        mock_geocode.return_value = Mock(latitude=40.7128, longitude=-74.0060)
        response = self.client.get(reverse('map_view'))
        self.assertEqual(response.status_code, 200)
        # Add assertions for checking the rendered map context

    @patch('geopy.geocoders.Nominatim.geocode')
    def test_map_viewSubmit(self, mock_geocode):
        mock_geocode.return_value = Mock(latitude=40.7128, longitude=-74.0060)
        response = self.client.get(reverse('map_viewSubmit'))
        self.assertEqual(response.status_code, 200)
        # Add assertions for checking the context returned by map_viewSubmit


