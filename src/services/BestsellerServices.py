from model.Bestseller import Bestseller

class BestsellerServices:

    def get_bestseller_by_id_service(self, productID):
        bestsellerOBJ = Bestseller().get_bestseller_by_id(productID)
        if not bestsellerOBJ:
            bestsellerOBJ = {"category": None,
                    "productID": None,
                    "totalSold": None}
        return bestsellerOBJ