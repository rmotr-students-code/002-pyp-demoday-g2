import requests
from instagram.client import InstagramAPI
import tweepy
from instance.config import Google_API, Insta_Client_ID, Insta_Client_Secret
from instance.config import Twitter_API_Key, Twitter_API_Secret, \
                            Twitter_Token, Twitter_Token_Secret

class GlocalAPI:
    def __init__(self, st_num, st_name, st_type, city, state, miles='1'):
        self.st_num = str(st_num)
        self.st_name = str(st_name)
        self.st_type = str(st_type)
        self.city = str(city)
        self.state = str(state)
        if miles != '1':
            self.miles = str(miles)
        else:
            self.miles = '1'  # default of 1 mile

        """
        HTTP GET request used to query Google Maps to convert an address into
        latitude, longitude coordinates. The GET request queries a specific
        Google Maps url (provided in the Google Maps API) with specific
        parameters attached (the address).
        """
        r = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address=' +
            self.st_num + '+' + self.st_name + '+' + self.st_type + ',+' +
            self.city + ',+' + self.state + '&sensor=FALSE' + Google_API)

        # Converts the data into readable json format
        data = r.json()

        # Pulls the latitude, longitude coords from a long stream of json data
        # that includes information other than the coordinates.
        self.latitude = data['results'][0]['geometry']['location']['lat']
        self.longitude = data['results'][0]['geometry']['location']['lng']

    def get_coordinates(self):
        return self.latitude, self.longitude

    def get_tweets(self):
        """
        Queries Tweets using Twitter API 'geocode' coordinates, which takes the
        parameters "latitude,longitude,radius" as strings. Assembles all of the
        search results into a list of tweets in the form of "Username: Tweet".
        Tweets are comprised of 'fields' (tweet, username,
        shared links, hashtag, etc. For example, tweet.text returns the
        'text' field of the tweet, tweet.user.screen_name returns the screen
        name of the tweeter.
        """
        # authenticates Twittery queries
        self.auth = tweepy.OAuthHandler(Twitter_API_Key, Twitter_API_Secret)
        self.auth.set_access_token(Twitter_Token, Twitter_Token_Secret)
        self.twitter_api = tweepy.API(self.auth)
        local_tweets = (self.twitter_api.search(geocode='{0},{1},{2}mi'.format(
                        self.latitude, self.longitude, self.miles)))
        lst_local_tweets = []
        # Assembles all of the search results into a list of tweets in the form of
        # "Username: Tweet". Tweets are comprised of 'fields' (tweet, username,
        # shared links, hashtag, etc. For example, tweet.text returns the 'text'
        # field of the tweet, tweet.user.screen_name returns the screen name of the
        # tweeter.
        for tweet in local_tweets:
            lst_local_tweets.append(tweet)
        return lst_local_tweets

    def get_instagram(self):
        """
        Queries latitude, longitude coordinates from Google Maps API using an
        address
        """

        # established link to Instagram using client ID and client secret
        instagram_api = InstagramAPI(client_id=Insta_Client_ID,
                                     client_secret=Insta_Client_Secret)
        # queries instagram images using Instagram API with geographic param
        # latitude and longitude as floats, and radius as a string
        local_media = instagram_api.media_search(count=20,
                                                 lat=self.latitude,
                                                 lng=self.longitude,
                                                 distance=self.miles + "km")

        # appends list of image links to 'photos' list. The image links are to
        # 'standard resolution' versions of images, not thumbnails.
        photos = []
        for media in local_media:
            photos.append(media.images['standard_resolution'].url)
        return photos


    def __str__(self):  # , st_num, st_name, st_type, city, state, miles):
        """
        String representation of class
        """
        return "Here are your parameters: {}, {}, {}, {}, {}, {}.".format(
            self.st_num,
            self.st_name,
            self.st_type,
            self.city,
            self.state,
            self.miles)
