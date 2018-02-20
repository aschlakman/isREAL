"""
Handle search keywords for the crawler
"""
import requests


DEFAULT_TAGS = ['#GazaPrison',
                '#freePalestine',
                # '#BDS -#BDSfail',
                '#iamgaza',
                '#PrayForPalestine',
                '#GazaUnlivable',
                '#Boycottisrael',
                '#FuckIsrael']


class TagGetter(object):
    def __init__(self):
        self.db_address = 'http://isreal-app.herokuapp.com'

    def get_tags(self, limit=10):
        response = requests.post('{db_address}/tags/get'.format(db_address=self.db_address))
        tags = ['#' + r["_id"] for r in response.json()["data"] if r["_id"].lower() not in ["israel"]]
        return tags[:limit]


class StreamKeywordManager(object):
    def __init__(self):
        """
        Manage the parameters used to search and stream new statuses
        """
        self.track = ['#freePalestine',
                      '#BDS -#BDSfail',
                      '#iamgaza',
                      '#Boycottisrael',
                      '#FuckIsrael']
        self.follow = ['freePalestine',
                       'PalestineToday',
                       'palestine',
                       'GlouthGraham',
                       'NationalSJP',
                       'BDSmovement',
                       'Col_Connaughton']
        # These must be converted to userID
        self.follow = []
        self.languages = ['en']

        self.filter_level = 'medium'


class SearchKeywordManager(object):
    def __init__(self):
        """
        Manage the parameters used to search and stream new statuses
        """
        self.tags = ['#GazaPrison',
                     '#freePalestine',
                     # '#BDS -#BDSfail',
                     '#iamgaza',
                     '#PrayForPalestine',
                     '#GazaUnlivable',
                     '#Boycottisrael',
                     '#FuckIsrael']
        self.users = ['@freePalestine',
                      '@PalestineToday',
                      '@palestine',
                      # '@GlouthGraham',
                      '@NationalSJP',
                      '@BDSmovement',
                      # '@Col_Connaughton'
                      ]
        self.users = []
        self.users = map(lambda username: 'from:' + username, self.users)
        self.lang = 'en'

    def q(self):
        """
        Generate query from keywords
        :return: query string
        """
        q = ' OR '.join(self.tags)
        # if self.tags and self.users:
        #     q += ' OR '
        # q += ' OR '.join(self.users)
        return q


class DynamicSearchManager(SearchKeywordManager):
    def __init__(self):
        super(DynamicSearchManager, self).__init__()
        self.tag_getter = TagGetter()

    def q(self):
        self.tags = self.tag_getter.get_tags()
        return super(DynamicSearchManager, self).q()
