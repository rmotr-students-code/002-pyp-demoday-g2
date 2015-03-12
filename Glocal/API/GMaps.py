from instance.config import Google_API
import requests

def get_coordinates(st_num, st_name, st_type, city, state):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + st_num + '+' + st_name + '+' + st_type + ',+' + city + ',+' + state + '&sensor=FALSE' + Google_API)
    data = r.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude

