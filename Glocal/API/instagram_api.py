# CLIENT ID	7bf46e4c3fb04d0188df8cf469133a0d
# CLIENT SECRET	3cee2195e2e040a5b77966b3b062fe40
# WEBSITE URL	http://kelseypaulo.blogspot.com/
# REDIRECT URI	http://kelseypaulo.blogspot.com/

# http://stackoverflow.com/questions/26288687/python-instagram-api-example-not-working
# https://github.com/Instagram/python-instagram

from instagram.client import InstagramAPI
# from


instagram_access_token = "3cee2195e2e040a5b77966b3b062fe40"
api = InstagramAPI(access_token=instagram_access_token)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)  # Get this error: instagram.bind.InstagramClientError: (404) Unable to parse response, not valid JSON.
for media in recent_media:
    print(media.caption.text)