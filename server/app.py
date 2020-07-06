from flask import Flask
from flask_restful import Resource, Api

from routes.BestsellerAPI import BestsellerAPI 

app = Flask(__name__)
api = Api(app)

#routes
api.add_resource(BestsellerAPI, "/checkifbestseller/<string:productID>")

if __name__ == '__main__':
    app.run(debug=True)