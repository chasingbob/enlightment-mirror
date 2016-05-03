import json
import requests

with open('config.json', 'r') as f:
    config = json.load(f)

def get_current_weather():
    key = config['weatherapi_key']
    id = 993800
    url = 'http://api.openweathermap.org/data/2.5/weather?id={0}&units=metric&appid={1}'.format(id,key)
    d = requests.get(url)
    url = 'http://openweathermap.org/img/w/{0}.png'.format(d.json()['weather'][0]['icon'])
    temp = d.json()['main']['temp']
    desc = d.json()['weather'][0]['description']
    return temp, desc, url