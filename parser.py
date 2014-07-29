from lxml import etree
from itertools import izip_longest

from config import MONGO_STORAGE_INPUT_DICT
from models import insert

class FParser(object):
    def __init__(self, page, pformat='html'):
        self.data = page.replace('<b>','').replace('</b>','')
        self.data_format = pformat
        self.dom = etree.HTML(self.data)
        self.products_xpath = '//div[@id="products"]'
        self.product_col_xpath = '//div[@class="gd-col gu3"]'
        self.title_path = '//a[@data-tracking-id="prd_title"]/text() | //a[@class="lu-title"]/text()'
        #ratings xpath are approximate only not perfect
        self.ratings_path = '//div[@class="pu-rating"]/text() | //div[@class="rating-wrapper"]/text()'
        self.price_path = '//span[@class="fk-font-17 fk-bold"]/text() | //div[@class="pu-final fk-font-17 fk-bold"]/text()'
        self.product_url = '//a[@data-tracking-id="prd_title"]/@href | //a[@class="lu-title"]/@href'

    def __parse(self):
        pass

    def get_all_cols(self, xp):
        self.prod = self.dom.xpath(self.products_xpath)
        if self.prod:
            self.prod = self.prod[0]
            return self.prod.xpath(xp) 

    def __get_matches_list(self, dom, _xpath):
        return [_.strip() for _ in dom.xpath(_xpath)]

    def items(self):
      
        pitems = self.get_all_cols(self.product_col_xpath)
        if pitems:
            #Grid view
            titles = self.__get_matches_list(pitems[0], self.title_path)
            ratings = self.__get_matches_list(pitems[0], self.ratings_path)
            prices = self.__get_matches_list(pitems[0], self.price_path)
            landing_page_url = self.__get_matches_list(pitems[0], self.product_url)
        else:
            #list view
            titles = self.__get_matches_list(self.prod, self.title_path)
            ratings = self.__get_matches_list(self.prod, self.ratings_path)
            prices = self.__get_matches_list(self.prod, self.price_path)
            landing_page_url = self.__get_matches_list(self.prod, self.product_url)
            
        #ratings is approximate, so in izip we have to put it at last
        for i in izip_longest(titles,prices,landing_page_url,ratings):
            yield i
    
    def store(self):
        for i in self.items():
            if i:
                data_layer = MONGO_STORAGE_INPUT_DICT
                #order is important
                data_layer['name'],data_layer['price'],data_layer['url'],data_layer['rating'] = i
                insert(data_layer)

"""
data = open('out.html','rb').read()
fp = FParser(data)
for i in fp.items():
    if i:
        data_layer = MONGO_STORAGE_INPUT_DICT
        data_layer['name'],data_layer['price'],data_layer['rating'],data_layer['url'] = i
        insert(data_layer)
"""