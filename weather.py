import json
import requests

def get_key():
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config['openweather_key']

def get_current_weather():
    key = get_key()
    pairs = {'id' : 993800, 'units' : 'metric', 'appid' : key}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    d = requests.get(url, params = pairs)
    temp = d.json()['main']['temp']
    desc =  d.json()['weather'][0]['description']
    icon = d.json()['weather'][0]['icon'] 
    icon_path = 'http://openweathermap.org/img/w/{0}.png'.format(icon)
       
    return temp,desc,icon_path

