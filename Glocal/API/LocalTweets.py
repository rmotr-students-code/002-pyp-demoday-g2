"""
Tweepy docs: Geolocalization: The search operator “near” isn’t available in API, but there is a more
precise way to restrict your query by a given location using the geocode parameter specified
with the template “latitude,longitude,radius”, for example, “37.781157,-122.398720,1mi”.
When conducting geo searches, the search API will first attempt to find tweets which have lat/long
within the queried geocode, and in case of not having success, it will attempt to find tweets created
by users whose profile location can be reverse geocoded into a lat/long within the queried geocode,
meaning that is possible to receive tweets which do not include lat/long information.
"""

# This doesn't work for me...
# from instance.config import Twitter_API_Key, Twitter_API_Secret, Twitter_Token, Twitter_Token_Secret
# from Glocal.API import GMaps


# This works
import GMaps
import tweepy

# Guetto fix
Twitter_API_Key = 'XpP7VNPUUak2YMMjZkW0sKA15'
Twitter_API_Secret = '2WOkIe7KkZ2B36bVcUsBEZA31LKQqHgCPWJJAF17G3E6ttZXrP'
Twitter_Token = '776228798-XCOTz36pFolEUeygxt7Os19oY3GgQSaCH2TriwKM'
Twitter_Token_Secret = 'jn43lDUZEDcoHSxmy20v2oR3EsoBdgXPwUlxni8OzOuUv'
Google_API = 'AIzaSyDBpDaj4GWXn8ApFULeB0GkvYTLWROpxVA'

auth = tweepy.OAuthHandler(Twitter_API_Key, Twitter_API_Secret)
auth.set_access_token(Twitter_Token, Twitter_Token_Secret)
api = tweepy.API(auth)

# temporary address below. To replace with user inputs in html form
# latitude, longitude = GMaps.get_coordinates("2300", "N Commonwealth", "Ave", "Chicago", "IL")


def get_local_tweets(lat, long):
    """
    This function uses the search method of the tweepy class passing the geocode parameter as a string.
    The geocode parameter takes the following arguments:
    :param lat: latitude
    :param long: longitude
    :return: long twitter string
    """
    local_tweets = api.search(geocode=str(lat) + ',' + str(long) + ',' + "1mi")
    return local_tweets

# example data table
address_list = [("2300", "N Commonwealth", "Ave", "Chicago", "IL"),  # (41.92417200000001, -87.638408)
                ("419", "Olavo Bilac", "Rua", "Campinas", "Sao Paulo"),  # (-22.8922579, -47.0563872)
                ("0", "Plaza del Cardenal Belluga", "Plaza", "Murcia", "Murcia"),  # (37.9848176, -1.129688)
                ("523", "Rua Afonso de Freitas", "Rua", "Sao Paulo", "Sao Paulo"),  # (-23.5762288, -46.6468314)
                ]

# prints some data using data from table. Uses both GMaps and also Tweeter
for st_num, st_name, st_type, city, state in address_list:
    latitude, longitude = GMaps.get_coordinates(st_num, st_name, st_type, city, state)
    print(get_local_tweets(latitude, longitude))  # long tweet message...
    # print(api.geo_id())# id string
    # t = tweepy.StreamListener()  # testing this
    # print(api.trends_closest(latitude, longitude))  # [{'parentid': 23424977, 'url': 'http://where.yahooapis.com/v1/place/2379574', 'country': 'United States', 'woeid': 2379574, 'name': 'Chicago', 'countryCode': 'US', 'placeType': {'code': 7, 'name': 'Town'}}]
    # print(api.reverse_geocode(latitude, longitude)[0])  # this uses the lat and long to return the location.


