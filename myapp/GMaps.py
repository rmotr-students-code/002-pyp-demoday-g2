__author__ = 'Mike Azar'

from config import API
import requests
import json

def get_coordinates(StNum,StName,StType,City, State):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + StNum + '+' + StName + '+' + StType + ',+' + City + ',+' + State + '&sensor=FALSE' + API)
    data = r.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude
