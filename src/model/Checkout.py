from .DB import DB

class Checkout(DB):

    def __init__(self):
        super(Checkout, self).__init__()

    def get_all_checkout(self):
        return self.db.checkout.find()