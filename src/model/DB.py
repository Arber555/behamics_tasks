from config.DataBase import DataBase

class DB:
    def __init__(self):
        self.db = DataBase("mongodb://localhost:27017/Behamics_DB", "Behamics_DB").conn()