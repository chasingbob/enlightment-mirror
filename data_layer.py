import json
from urllib.parse import urlparse
import urllib
import requests
import config

def get_key(key):
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config[key]

def get_current_weather_data():
    key = get_key('openweather_key')
    pairs = {'id' : 993800, 'units' : 'metric', 'appid' : key}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    result = requests.get(url, params = pairs)

    return result.json()


def get_weather_forecast_data():
    key = get_key('openweather_key')
    pairs = {'id' : 993800, 'units' : 'metric', 'appid' : key }
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    result = requests.get(url, params = pairs)

    return result.json()

def get_traffic_data():
    key = get_key('google_key')
    origin = config.get_value('origin').replace(' ','+')
    destination = config.get_value('destination').replace(' ','+')

    pairs = { 'origins' : origin, 'destinations' : destination, 'departure_time' : 'now', 'traffic_model' : 'pessimistic', 'key' : key}
    result = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params = pairs)

    return result.json()
