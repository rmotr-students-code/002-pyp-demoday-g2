from Glocal.instance.config import Insta_Client_ID, Insta_Client_Secret
from instagram.client import InstagramAPI
from Glocal.API import google_maps

def get_local_instagram(st_num,st_name,st_type,city,state,miles):
    # queries latitude, longitude coordinates from Google Maps API using an
    # address
    latitude, longitude = google_maps.get_coordinates(st_num, st_name, st_type,
                                                      city, state)
    # established link to Instagram using client ID and client secret
    api = InstagramAPI(client_id=Insta_Client_ID,
                       client_secret=Insta_Client_Secret)
    # queries instagram images using Instagram API with geographic parameters
    # latitude and longitude as floats, and radius as a string
    local_media = api.media_search(count=20, lat=latitude, lng=longitude,
                                   distance=str((miles))+"km")
    # appends list of image links to 'photos' list. The image links are to
    # 'standard resolution' versions of images, not thumbnails.
    photos = []
    for media in local_media:
        photos.append(media.images['standard_resolution'].url)
    return photos

# get_local_instagram("1500", "massachusetts","avenue","washington","DC",2)
