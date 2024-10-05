from django.shortcuts import render
import requests
from django.conf import settings
import datetime

def home(request):
    city = request.GET.get('city', 'Bhubaneswar')  # Default city is Bhubaneswar
    api_key = '9c754ff7adde07256ded98d998ed7afd'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:
        data = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
            'datetime': datetime.datetime.now(),
        }
    else:
        data = {
            'error': 'City not found or unable to fetch data. Please try again.',
        }

    return render(request, 'index.html', data)
