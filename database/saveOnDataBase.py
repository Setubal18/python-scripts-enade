from pymongo import MongoClient

from settings import MONGO_URI, DATABASE, COLLECTION

client = MongoClient(MONGO_URI)
db = client[DATABASE]
enade_collentions = db[COLLECTION]

def create(dict):
    if not enade_collentions.find_one({'index': dict['index']}):
        enade_collentions.insert_one(dict)
    else:
        print('Já existe')
