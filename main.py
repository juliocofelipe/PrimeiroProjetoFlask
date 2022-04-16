from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.item import Items, Item

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Items, '/items')
api.add_resource(Item, '/items', '/items/<string:product>')


if __name__=="__main__":
  from sql_alchemy import db
  db.init_app(app)
  app.run(host='0.0.0.0', port=8080, debug=True)


