from pymongo import MongoClient

from settings import MONGO_URI, DATABASE, COLLECTION
from standardization_of_data import execute

client = MongoClient(MONGO_URI)
db = client[DATABASE]
enade_collentions = db[COLLECTION]


def receiveData():
    dados = execute()
    print(dados)
    for dict in dados:
        create(dict)


def create(dict):
    if not enade_collentions.find_one({'index': dict['index']}):
        enade_collentions.insert_one(dict)
    else:
        print('Já existe')


receiveData()
