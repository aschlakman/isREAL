import tweepy
import requests
from isreal.credentials import consumer_key, consumer_secret, access_token, access_token_secret
from isreal.crawler.stream import Crawler


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StatusInserter(object):
    def __init__(self):
        self.db_address = 'http://192.168.0.121:8001'

    def retrive_status_data(self, status):
        """
        get the data required for the db from the tweet representation
        :param status: Status (by Tweepy)
        :return: dict
        """
        status_data_dict = dict()
        status_data_dict['url'] = 'https://twitter.com/{username}/status/{id}'.format(username=status.user.screen_name,
                                                                                      id=status.id_str)
        status_data_dict['likes'] = status.favorite_count
        status_data_dict['retweets'] = getattr(status, 'retweet_count', 0)
        status_data_dict['tweetPostingTime'] = status.created_at.strftime('%Y:%m:%d %H:%M:%S')
        status_data_dict['authorUserName'] = status.user.name
        status_data_dict['authorDisplayName'] = status.user.screen_name
        status_data_dict['tags'] = [hashtag['text'] for hashtag in status.entities['hashtags']]
        status_data_dict['userId'] = status.user.id_str

        return status_data_dict

    def write_status_to_db(self, status):
        """
        get a status representation of the tweet and insert to the joint DB
        :param status: Status (by Tweepy)
        """
        data_to_write = self.retrive_status_data(status=status)
        requests.post('{db_address}/posts/add'.format(db_address=self.db_address), json=data_to_write)

    def write(self, status):
        dic = self.retrive_status_data(status)
        print(dic)

    def work(self):
        while True:
            statuses_to_add =


th = StatusesHandler()
th.work()
# for tweet in tweepy.Cursor(api.search, q='isREALiBot').items(3):
#     th.write(tweet)




