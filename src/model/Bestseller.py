from .DB import DB

class Bestseller(DB):

    def __init__(self):
        super(Bestseller, self).__init__()

    def get_all_bestseller(self):
        return self.db.bestseller.find()

    def add_bestsellers(self, data):
        self.db.bestseller.insert_many(data)

    def get_bestseller_by_id(self, id):
        try:
            bestseller = self.db.bestseller.find_one({"productID": id})
        except:
            print("No product found")
        return bestseller