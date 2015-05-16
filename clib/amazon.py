
class BaseCrawler(object):
    url = ""
    
    def next_page_url(self, page_num=1):
        raise NotImplementedError("Implement")
    
class Crawler(BaseCrawler):
    url = "http://www.amazon.in/s/ref=sr_pg_4?&page={page}&keywords={search}"
    current_page = 1
    search = None

    @classmethod
    def absolute_url(cls, search, page_num=1):
        cls.search = search
        return Crawler.url.format(search=search, page=page_num)

    @classmethod
    def next_page_url(cls, page_num=1):
        Crawler.current_page += 1
        return Crawler.absolute_url(cls.search, page_num=Crawler.current_page)
