import pymongo
import pandas as pd
from pymongo import MongoClient
from itertools import chain

class DataManipulation:

    def db_connection(self):
        cluster = MongoClient("mongodb://localhost:27017/")
        db = cluster["Behamics_DB"]

        return db

    def most_sold_products(self):
        '''
            Extract 20% of the most sold products (productID) per category.
            And save the data for each extracted product in the collection 
            bestseller with fields: productID, category, totalSold.
        '''
        conn = self.db_connection()
        checkout = conn.checkout.find()
        data_frame = pd.DataFrame(list(checkout))

        carts = pd.DataFrame(list(chain.from_iterable(list(data_frame["cart"]))))

        x = carts.groupby(['category','productID'])['productID'].agg(['count']).reset_index()
        x.groupby(["category"])['category'].agg(['count'])
        data = (x.groupby('category',group_keys=False)
                .apply(lambda x: x.nlargest(int(len(x) * 0.2), 'count')))
        data.columns = ['category','productID','totalSold']
        
        conn.bestseller.insert_many(data.to_dict('records'))