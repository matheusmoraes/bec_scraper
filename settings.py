import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)) 

mongo_url = 'mongodb+srv://%s:%s@cluster0-u81tj.mongodb.net/test'
mongo_settings = {'username': '', 'password': ''}

try:
    from local_settings import mongo_settings
except(ImportError):
    pass
