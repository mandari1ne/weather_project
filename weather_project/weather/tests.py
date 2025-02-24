from django.test import TestCase
from .models import Weather

# Create your tests here.

class TestWeatherCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Weather.objects.create(
            city='Minsk',
            temperature=10.6,
            description='clear sky'
        )

    def test_get(self):
        self.assertEqual(str(Weather.objects.get(id=1)), 'Minsk - 10.6°C')

    def test_timestamp(self):
        self.assertIsNotNone(Weather.objects.get(id=1).timestamp)

class TestWeatherView(TestCase):
    def test_get_weather_view(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather_index.html')

    def test_weather_view_post(self):
        response = self.client.post('', {'city': 'Minsk'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Weather in Minsk')
