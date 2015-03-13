from instance.config import Twitter_API_Key, Twitter_API_Secret, Twitter_Token, Twitter_Token_Secret
from Glocal.API import GMaps
import tweepy

auth = tweepy.OAuthHandler(Twitter_API_Key, Twitter_API_Secret)
auth.set_access_token(Twitter_Token, Twitter_Token_Secret)
api = tweepy.API(auth)

#temporary address below. To replace with user inputs in html form
latitude, longitude = GMaps.get_coordinates("1500","Massachusetts","Ave","Washington","DC")

local_tweets = api.search(geocode=str(latitude) + ',' + str(longitude) + ',' + "1mi")
