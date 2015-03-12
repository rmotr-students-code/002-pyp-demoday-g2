# CLIENT ID	7bf46e4c3fb04d0188df8cf469133a0d
# CLIENT SECRET	3cee2195e2e040a5b77966b3b062fe40
# WEBSITE URL	http://kelseypaulo.blogspot.com/
# REDIRECT URI	http://kelseypaulo.blogspot.com/


from instagram.client import InstagramAPI

access_token = "YOUR_ACCESS_TOKEN"
api = InstagramAPI(access_token=access_token)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
    print (media.caption.text)