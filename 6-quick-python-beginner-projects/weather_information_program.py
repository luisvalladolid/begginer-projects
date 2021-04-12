import requests
from pprint import pprint

API_Key = 'fbe7095ab0006e3b6f5841bed3165631'

city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)
