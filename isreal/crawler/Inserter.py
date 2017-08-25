from datetime import datetime
from time import sleep

import tweepy
import requests
from isreal.credentials import consumer_key, consumer_secret, access_token, access_token_secret
from isreal.crawler.search import Crawler
from isreal.keywords import DynamicSearchManager


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StatusInserter(object):
    def __init__(self):
        self.db_address = 'http://192.168.1.101:8002'  # 'http://192.168.0.138:8001'
        self.Crawler = Crawler()
        self.Crawler.keyword_manager = DynamicSearchManager()

    def retrive_status_data(self, status):
        """
        get the data required for the db from the tweet representation
        :param status: Status (by Tweepy)
        :return: dict
        """
        status_data_dict = dict()
        status_data_dict['tweetId'] = status.id_str
        status_data_dict['text'] = status.text
        status_data_dict['likes'] = status.favorite_count
        status_data_dict['retweets'] = getattr(status, 'retweet_count', 0)
        status_data_dict['tweetPostingTime'] = status.created_at.strftime('%Y:%m:%d %H:%M:%S')
        status_data_dict['authorUserName'] = status.user.name
        status_data_dict['authorDisplayName'] = status.user.screen_name
        status_data_dict['authorFollowers'] = status.user.followers_count
        status_data_dict['tags'] = [hashtag['text'] for hashtag in status.entities['hashtags']]
        status_data_dict['authorId'] = status.user.id_str
        status_data_dict['searchType'] = 'mixed'
        return status_data_dict

    def write_status_to_db(self, status, search_type):
        """
        get a status representation of the tweet and insert to the joint DB
        :param status: Status (by Tweepy)
        """
        data_to_write = self.retrive_status_data(status=status)
        if search_type != 'mixed':
            data_to_write['searchType'] = 'popular'
        try:
            if self.db_address:
                response = requests.post('{db_address}/posts/add'.format(db_address=self.db_address), json=data_to_write)
                print(str(response.content))
            print("=====================================")
            print("@" + status.user.screen_name, "Retweets: " + str(status.retweet_count),
                  "Favorites: " + str(status.favorite_count), "Followers: " + str(status.user.followers_count))
            print(status.text)
            sleep(2)

        except requests.exceptions.ConnectionError as e:
            print("Got Connection Error", e)

    def write(self, status):
        dic = self.retrive_status_data(status)
        print(dic)

    def work(self):
        popular_count = 0
        while True:
            if popular_count == 0:
                search_type = 'popular'
                popular_count = 100
            else:
                search_type = 'mixed'
                popular_count -= 1
            try:
                statuses_to_add = self.Crawler.search(search_type)
            except tweepy.RateLimitError:
                print("Hit Rate Limit")
                sleep(15 * 60)

            for status in statuses_to_add:
                self.write_status_to_db(status, search_type)

if __name__ == '__main__':
    th = StatusInserter()
    th.work()




