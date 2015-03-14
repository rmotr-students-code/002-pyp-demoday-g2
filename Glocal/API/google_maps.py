from instance.config import Google_API
import requests

def get_coordinates(st_num, st_name, st_type, city, state):
    # HTTP GET request used to query Google Maps to convert an address into latitude, longitude coordinates. The GET request queries
    # a specific Google Maps url (provided in the Google Maps API) with specific parameters attached (the address).
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + st_num + '+' + st_name + '+' + st_type + ',+' + city + ',+' + state + '&sensor=FALSE' + Google_API)
    # Converts the data into readable json format
    data = r.json()
    # Pulls the latitude, longitude coordinates from a long stream of json data that includes information other than the coordinates.
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude

