__author__ = 'Mike Azar'

from instance.config import Google_API

def get_coordinates(StNum,StName,StType,City, State):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + StNum + '+' + StName + '+' + StType + ',+' + City + ',+' + State + '&sensor=FALSE' + Google_API)
    data = r.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude
