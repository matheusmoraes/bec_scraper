from settings import mongo_settings, mongo_url
from pymongo import MongoClient
from log import log

class Storage():

    def __init__(self):
        log.info('Connecting to MongoCloud')
        connect_url = mongo_url % (mongo_settings['username'], 
                mongo_settings['password'])
        self.client = MongoClient(connect_url)
        self.db = self.client.bec

    def save_item(self, item):
        log.info('Saving item %s' % item)
        self.db.items.insert_one(item)

    def save_items(self, items):
        log.info('Bulk saving %i items' % len(items))
        self.db.items.insert_many(items)
        
