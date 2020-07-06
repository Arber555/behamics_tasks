import pandas as pd
from itertools import chain
from model.Checkout import Checkout
from model.Bestseller import Bestseller

class DataManipulation:

    def most_sold_products(self):
        '''
            Extract 20% of the most sold products (productID) per category.
            And save the data for each extracted product in the collection 
            bestseller with fields: productID, category, totalSold.
        '''
        checkout = Checkout().get_all_checkout()
        data_frame = pd.DataFrame(list(checkout))

        carts = pd.DataFrame(list(chain.from_iterable(list(data_frame["cart"]))))

        x = carts.groupby(['category','productID'])['productID'].agg(['count']).reset_index()
        x.groupby(["category"])['category'].agg(['count'])
        data = (x.groupby('category',group_keys=False)
                .apply(lambda x: x.nlargest(int(len(x) * 0.2), 'count')))
        data.columns = ['category','productID','totalSold']
        
        Bestseller().add_bestsellers(data.to_dict('records'))
