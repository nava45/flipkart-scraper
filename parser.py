from lxml import etree

class FParser(object):
    def __init__(self, page, pformat='html'):
        self.data = page.replace('<b>','').replace('</b>','')
        self.data_format = pformat
        self.dom = etree.HTML(self.data)
        self.products_xpath = '//div[@id="products"]'
        self.product_col_xpath = '//div[@class="gd-col gu3"]'
        self.title_path = '//a[@data-tracking-id="prd_title"]/text()'
        self.ratings_path = '//div[@class="pu-rating"]/text()'
        self.price_path = '//span[@class="fk-font-17 fk-bold"]/text()'

    def __parse(self):
        pass

    def get_all_cols(self, xp):
        prod = self.dom.xpath(self.products_xpath)
        if prod:
            prod = prod[0]
            return prod.xpath(xp) 

    def items(self, xpath_string):
        #ctx = etree.iterwalk(self.__extracted_dom(xpath_string), events=('start',))
        #products = []

        pitems = self.get_all_cols(self.product_col_xpath)
        if pitems:
            return pitems
        
        #return products



products_xpath = "//div[@id='products']"

data = open('out.html','rb').read()
fp = FParser(data)
print fp.items(products_xpath)
