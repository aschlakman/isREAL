import tweepy

from isreal.credentials import *
from isreal.keywords import KeywordManager

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class Crawler(object):
    def __init__(self, on_status, keyword_manager=KeywordManager()):
        """
        Find statuses on twitter using keyword searches. on_status is called whenever a status is found
        Example:
        >>>def on_status(status):
        >>>    print('Tweet by: @' + status.user.screen_name, "Num of followers:" + str(status.user.followers_count))
        >>>c = Crawler(on_status)

        :param on_status: function to call when a new status is found
        :param keyword_manager: object in charge of supplying keywords to search
        """
        stream_listener = tweepy.StreamListener()
        stream_listener.on_status = on_status

        self.stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        self.stream.filter(track=keyword_manager.track, follow=keyword_manager.follow,
                           languages=keyword_manager.languages, async=True)

    def disconnect(self):
        """
        Stop crawler
        """
        self.stream.disconnect()
