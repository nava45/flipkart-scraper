from pymongo import Connection
from datetime import datetime

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
