from lxml import etree

class FParser(object):
    def __init__(self, page, pformat='html'):
        self.data = page
        self.data_format = pformat
        self.dom = etree.HTML(self.data)

    def __parse(self):
        pass

    def __extracted_dom(self, xpath):
        res = self.dom.xpath(xpath)
        return res[0] if res else None
    
    def items(self, xpath_string):
        ctx = etree.iterwalk(self.__extracted_dom(xpath_string), events=('start',))
        products = []
        for event,element in ctx:
            item_layer = {'id':'','name':'','price':'','rating':'','available':'', 'text':''}
            if element.attrib.has_key('id'):
                print element.attrib,element.tag
                print "*" * 20
                if element.attrib['id']:
                    item_layer['id'] = element.attrib['id']
                    products.append(item_layer)
                    s = ''
                    for i in element.itertext():
                        s += i.strip()
                    item_layer['text'] = s
             

        return products



products_xpath = "//div[@id='products']"

data = open('out.html','rb').read()
fp = FParser(data)
print fp.items(products_xpath)
