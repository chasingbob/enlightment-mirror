import json
from urllib.parse import urlparse
import urllib
import requests
import config


#!/usr/bin/env python3
#!python3

def get_key():
    return config.get_value('google_key')

def get_current_traffic(origin,destination):
    return '14', '32'
    #o = origin.replace(' ','+') 
    #d = destination.replace(' ','+')
    #key = get_key()
   
    #pairs = { 'origins' : o, 'destinations' : d, 'departure_time' : 'now', 'traffic_model' : 'pessimistic', 'key' : key}
    #result = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params = pairs)
    #print('result')    
    #print(result.json())
    #dist = result.json()['rows'][0]['elements'][0]['distance']['text']
    #dura = result.json()['rows'][0]['elements'][0]['duration_in_traffic']['text']
    #return dist, dura

