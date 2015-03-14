# !/usr/bin/env python3
#
# # from instance.config import Google_API
# # from Glocal.instance.config import Google_API
import requests

Google_API = 'AIzaSyDBpDaj4GWXn8ApFULeB0GkvYTLWROpxVA'

def get_coordinates(st_num, st_name, st_type, city, state):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + st_num + '+' + st_name + '+' + st_type + ',+' + city + ',+' + state + '&sensor=FALSE' + Google_API)
    data = r.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude



