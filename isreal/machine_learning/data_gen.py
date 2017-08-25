import json
from isreal.crawler.search import Crawler

c = Crawler()
# c.keyword_manager =
# found_statuses = c.search('popular')
found_statuses = []
for i in range(15):
    s = c.search('popular').next()
    found_statuses.append(s)

for i in range(45):
    s = c.search('mixed').next()
    found_statuses.append(s)
# found_statuses = [s for s in c.search('popular')] + [s for s in c.search('mixed')]
# found_statuses = found_statuses[:60]

status_to_data = dict()
status_to_rating = dict()

for status in found_statuses:
    status_to_data[status.id] = [status.text, status.favorite_count, status.retweet_count, status.user.followers_count]

    print(status.text, sep=',')
    print("=====================================")
    print("@" + status.user.screen_name, "Retweets: " + str(status.retweet_count),
          "Favorites: " + str(status.favorite_count), "Followers: " + str(status.user.followers_count))
    print(status.text)

with open('status_to_stats.json', 'w', encoding='utf-8') as f:
    json.dump(status_to_data, f)
