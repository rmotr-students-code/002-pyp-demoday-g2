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
import config_keys # this is where my keys are...

# Guetto fix for not having the instance folder
a = config_keys.Google_API # change the configs
Twitter_API_Key = config_keys.Twitter_API_Key
Twitter_API_Secret = config_keys.Twitter_API_Secret
Twitter_Token = config_keys.Twitter_Token
Twitter_Token_Secret = config_keys.Twitter_Token_Secret
Google_API = config_keys.Google_API



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


def get_url_from_tweets_address(st_num, st_name, st_type, city, state):
    """ Takes in data and gives back list of urls"""
    url_list = []
    latitude, longitude = GMaps.get_coordinates(st_num, st_name, st_type, city, state)
    long_tweet = get_local_tweets(latitude, longitude)
    for long_message in long_tweet: # can use list comp, but not too worried about it just now
        url_list.append(long_message.entities['urls'])
    for url in url_list:
        if not url:
            pass
        else:
            str_url = str(url).split()
            # print(str_url[1].replace("'", "").replace(",",""))
            return str_url[1].replace("'", "").replace(",", "")





# testing
# example data table
address_list = [("2300", "N Commonwealth", "Ave", "Chicago", "IL"),  # (41.92417200000001, -87.638408)
                ("419", "Olavo Bilac", "Rua", "Campinas", "Sao Paulo"),  # (-22.8922579, -47.0563872)
                ("0", "Plaza del Cardenal Belluga", "Plaza", "Murcia", "Murcia"),  # (37.9848176, -1.129688)
                ("523", "Rua Afonso de Freitas", "Rua", "Sao Paulo", "Sao Paulo"),  # (-23.5762288, -46.6468314)
                ]

for st_num, st_name, st_type, city, state in address_list:
    print(get_url_from_tweets_address(st_num, st_name, st_type, city, state))


def get_url_from_tweets_lat_long(lat, long):
    """ Takes in data and gives back list of urls"""
    pass


#########################
# url_list = []
# # prints some data using data from table. Uses both GMaps and also Tweeter
# for st_num, st_name, st_type, city, state in address_list:
#     latitude, longitude = GMaps.get_coordinates(st_num, st_name, st_type, city, state)
#     long_tweet = get_local_tweets(latitude, longitude)
#     for long_message in long_tweet:
#         # print(i.user.screen_name, "|")#, i.text)
#         url_list.append(long_message.entities['urls'])
#         # print(long_message.entities['urls'])
#
# for url in url_list:
#     if not url:
#         pass
#     else:
#         print(url)
#
# ########

# variable = get_local_tweets('41.92417200000001', '-87.638408')
# url_list = []
# for i in variable:
#     # print(i.user.screen_name, "|")#, i.text)
#     # print(i.entities['hashtags'])
#     #url_list.append(i)  # works
#     url_list.append(i.entities['urls'])
#     # print(i.entities['urls'])  # works
#
# for url in url_list:
#     if not url:
#         pass
#     else:
#         print(url)
# print(len(url_list))
########################

    # print(get_local_tweets(latitude, longitude))  # long tweet message...

    # print(api.geo_id())# id string
    # t = tweepy.StreamListener()  # testing this
    # print(api.trends_closest(latitude, longitude))  # [{'parentid': 23424977, 'url': 'http://where.yahooapis.com/v1/place/2379574', 'country': 'United States', 'woeid': 2379574, 'name': 'Chicago', 'countryCode': 'US', 'placeType': {'code': 7, 'name': 'Town'}}]
    # print(api.reverse_geocode(latitude, longitude)[0])  # this uses the lat and long to return the location.


