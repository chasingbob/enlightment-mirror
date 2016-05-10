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
    o = origin.replace(' ','+') 
    d = destination.replace(' ','+')
    key = get_key()

    #base = urlparse('https://maps.googleapis.com/maps/api/distancematrix/json')
    pairs = { 'origins' : o, 'destinations' : d, 'departure_time' : 'now', 'traffic_model' : 'pessimistic', 'key' : key}
   
    #call = '{0}?&origins={1}&destinations={2}&departure_time=now&traffic_model=pessimistic&key={3}'.format(url,o,d,key)
    result = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params = pairs)
    #result = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=8+bobby+locke+randburg&destinations=2+impala+ave+sandton&key=AIzaSyDHBCGUXVMR8iErDeLPIRgVmaJN2n61czQ')
    dist = result.json()['rows'][0]['elements'][0]['distance']['text']
    dura = result.json()['rows'][0]['elements'][0]['duration_in_traffic']['text']
    return dist, dura

#return 'blah'
