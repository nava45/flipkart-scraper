from pymongo import Connection, DESCENDING
from datetime import datetime
import re

class MongoException(Exception):
    def __init__(self, error):
        self.__msg = error.message

    def __str__(self):
        return repr(self.__msg)


def connect_to_db(collection=False):
    connection = Connection('localhost', 27017)
    db = connection['flipkart']
    try:
        if collection:
            return db.flipitems
        return db
    except Exception as e:
        raise MongoException(e)


def insert(input_dict):
    table = connect_to_db(collection=True)
    table.insert({'crawled_at':datetime.utcnow(),\
                  'name':input_dict.get('name',None),\
                  'price':input_dict.get('price',None),\
                  'rating':input_dict.get('rating',None),\
                    'url':input_dict.get('url',None)
              }, safe=True)


def fetch_by_name(name):
    print "Name:",name
    result = []
    table = connect_to_db(collection=True)
    regex = '.*'+name+'.*'
    for row in table.find({"name": re.compile(regex, re.IGNORECASE)}).sort('crawled_at',DESCENDING):
        result.append(row)
    return result