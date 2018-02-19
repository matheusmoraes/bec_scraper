from settings import mongo_settings, mongo_url
from pymongo import MongoClient

class Storage():

    def __init__(self):
        connect_url = mongo_url % (mongo_settings['username'], 
                mongo_settings['password'])
        self.client = MongoClient(connect_url)
        self.db = self.client.bec

    def save_item(self, item):
        self.db.items.insert_one(item)
        
