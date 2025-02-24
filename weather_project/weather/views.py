from django.shortcuts import render
from .models import Weather
import requests

# Create your views here.

def get_weather_data(city):
    API_KEY = '2f22d402173cb2c104f56d18e8c5aab9'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }

    return None

def weather_index(request):
    weather = None

    if request.method == 'POST':
        city = request.POST['city']
        weather = get_weather_data(city)

        if weather:
            Weather.objects.create(
                city=weather['city'],
                temperature=weather['temperature'],
                description=weather['description']
            )

    history = Weather.objects.all().order_by('-timestamp')

    return render(request, 'weather_index.html', {'weather': weather, 'history': history})
