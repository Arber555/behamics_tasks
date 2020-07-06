import json
from flask_restful import Resource
from bson import json_util

from services.BestsellerServices import BestsellerServices

class BestsellerAPI(Resource):
    def get(self, productID):
        bestsellerOBJ = BestsellerServices().get_bestseller_by_id_service(productID)
        return json.loads(json_util.dumps(bestsellerOBJ))