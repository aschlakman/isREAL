"""
Handle search keywords for the crawler
"""


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
        self.tags = ['#freePalestine',
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
