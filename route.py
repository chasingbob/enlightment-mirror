import json
import requests

with open('config.json', 'r') as f:
    config = json.load(f)
    
def get_distance_duration(from, to):
    key = config['google_key']
    base = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    call = "{0}?&origins={1}&destinations={2}&departure_time=now&traffic_model=pessimistic&key={3}".format(base,f.replace(' ','+'),t.replace(' ','+'),key)
    d = requests.get(call)
    distance = d.json()['rows'][0]['elements'][0]['distance']['text']
    duration = d.json()['rows'][0]['elements'][0]['duration_in_traffic']['text']
    
    return distance,duration
    
    
    