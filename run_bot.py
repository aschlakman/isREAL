from isreal.keywords import DynamicSearchManager, SearchKeywordManager
from isreal.crawler.Inserter import StatusInserter


si = StatusInserter()
# si.Crawler.keyword_manager = SearchKeywordManager()
# si.db_address = None
si.work()
