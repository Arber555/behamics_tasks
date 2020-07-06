from config.DataBase import DataBase

class Checkout(DataBase):

    def __init__(self):
        super(Checkout, self).__init__()

    def get_all_checkout(self):
        return self.db.checkout.find()