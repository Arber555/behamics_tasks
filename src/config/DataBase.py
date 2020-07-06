import pymongo
from pymongo import MongoClient

class DataBase:

    def __init__(self, url, db_name):
        self.url = url
        self.db_name = db_name

    def conn(self):
        cluster = MongoClient(self.url)
        db = cluster[self.db_name]

        return db