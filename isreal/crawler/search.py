import tweepy

from isreal.credentials import *
from isreal.keywords import SearchKeywordManager

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class Crawler(object):
    def __init__(self):
        """
        Find statuses using rest API
        """
        # object in charge of supplying keywords to search
        self.keyword_manager = SearchKeywordManager()

    def search(self, result_type='popular'):
        """
        Search for statuses
        :param result_type: can be 'popular', 'mixed' or 'recent'
        :raises: tweepy.RateLimitError if API rate was exceeded
        :return: list of statuses returned by search query
        """
        statuses = tweepy.Cursor(api.search, q=self.keyword_manager.q(), lang=self.keyword_manager.lang,
                                 result_type=result_type
                                 ).items()
        return statuses

    # Example script
    # c = Crawler()
    # # found_statuses = c.search('popular')
    # found_statuses = [s for s in c.search('popular')] + [s for s in c.search('mixed')]
    # found_statuses = found_statuses[:60]
    # for status in found_statuses:
    #     print(status.text, sep=',')
    #     print("=====================================")
    #     print("@" + status.user.screen_name, "Retweets: " + str(status.retweet_count),
    #           "Favorites: " + str(status.favorite_count), "Followers: " + str(status.user.followers_count))
    #     print(status.text)
