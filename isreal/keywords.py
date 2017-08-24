"""
Handle search keywords for the crawler
"""


class KeywordManager(object):
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
