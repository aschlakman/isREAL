"""
Example for getting tweets from a public stream
"""


import tweepy

from isreal.credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#  override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        print('Tweet by: @' + status.user.screen_name, "Num of followers:" + str(status.user.followers_count))
        print(status.created_at)
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['BDS'], async=True)
