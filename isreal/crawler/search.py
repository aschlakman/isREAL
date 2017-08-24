import tweepy

from isreal.credentials import *
from isreal.keywords import SearchKeywordManager

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

MAX_ITEMS = 100


class Crawler(object):
    def __init__(self, keyword_manager=SearchKeywordManager()):
        """
        Find statuses using rest API
        :param keyword_manager: object in charge of supplying keywords to search
        """
        self.keyword_manager = keyword_manager

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

if __name__ == '__main__':
    """
    Example script
    """
    c = Crawler()
    found_statuses = c.search('recent')
    for status in found_statuses:
        print("=====================================")
        print("@" + status.user.screen_name, "Retweets: " + str(status.retweet_count),
              "Favorites: " + str(status.favorite_count), "Followers: " + str(status.user.followers_count))
        print(status.text)
