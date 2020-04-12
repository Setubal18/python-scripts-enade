from pymongo import MongoClient
from formatDatas import execute

db = client.proictHomol
enade_collentions = db.enadeRespostas


def readData():
    dados = execute()
    print(dados)
    for dict in dados:
        create(dict)


def create(dict):
    if not enade_collentions.find_one({'index': dict['index']}):
        enade_collentions.insert_one(dict)
    else:
        print('Já existe')


readData()
