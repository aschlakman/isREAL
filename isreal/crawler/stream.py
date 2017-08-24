import tweepy

from isreal.credentials import *
from isreal.keywords import KeywordManager

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#  override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print('Tweet by: @' + status.user.screen_name, "Num of followers:" + str(status.user.followers_count))
        print(status.created_at, status.text)

keyword_manager = KeywordManager()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=keyword_manager.track, follow=keyword_manager.follow, languages=keyword_manager.languages,
                async=True)
