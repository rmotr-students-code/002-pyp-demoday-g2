from instance.config import Twitter_API_Key, Twitter_API_Secret, Twitter_Token, Twitter_Token_Secret
from Glocal.API import google_maps
import tweepy

# authenticates Twittery queries
auth = tweepy.OAuthHandler(Twitter_API_Key, Twitter_API_Secret)
auth.set_access_token(Twitter_Token, Twitter_Token_Secret)
api = tweepy.API(auth)


def get_local_tweets(st_num,st_name,st_type,city,state,miles):
    # queries latitude, longitude coordinates from Google Maps API using an address
    latitude, longitude = google_maps.get_coordinates(st_num,st_name,st_type,city,state)
    # queries Tweets using Twitter API 'geocode' coordinates, which takes the parameters "latitude,longitude,radius" as strings
    local_tweets = (api.search(geocode=str(latitude) + ',' + str(longitude) + ',' + miles + "mi"))
    lst_local_tweets = []
    # Assembles all of the search results into a list of tweets in the form of "Username: Tweet".
    # Tweets are comprised of 'fields' (tweet, username, shared links, hashtag, etc. For example, tweet.text returns the 'text'
    # field of the tweet, tweet.user.screen_name returns the screen name of the tweeter.
    for tweet in local_tweets:
        lst_local_tweets.append(tweet.user.screen_name + ": " + tweet.text)
    return lst_local_tweets

