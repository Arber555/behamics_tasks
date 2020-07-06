import pymongo
from pymongo import MongoClient

class DataBase:

    def __init__(self):
        cluster = MongoClient("mongodb://localhost:27017/")
        self.db = cluster["Behamics_DB"]