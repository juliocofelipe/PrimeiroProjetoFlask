from flask_restful import Resource, reqparse
from models.item import ItemModel

class Items(Resource):
  def get(self):
    return {'items': [item.json() for item in ItemModel.query.all()]}

class Item(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('product', required=True, help="The field 'Produto', cannot be left blank.")
  parser.add_argument('quantity')
  parser.add_argument('price')

  def get(self, item_id):
    item = ItemModel.find_item(item_id)
    if item:
      return item.json()
    return {'message': 'Item not found.'}, 404

  def post(self, item_id):
    if ItemModel.find_item(item_id):
      return {'message': "Item id {} already exists.".format(item_id)}, 400
    data = Item.parser.parse_args()
    item = ItemModel(item_id, **data)
    try:
      item.save_item()
    except:
      return {'message': 'An internal occurred while saving the item.'}, 500
    return item.json()

  def put(self, item_id):
    data = Item.parser.parse_args()
    item_found = ItemModel.find_item(item_id)
    if item_found:
      item_found.update_item(**data)
      item_found.save_item()
      return item_found.json(), 200
    item = ItemModel(item_id, **data)
    try:
      item.save_item()
    except:
      return {'message': 'An internal error ocurred while saving the item.'}, 500
    return item.json(), 201
  
  def delete(self, item_id):
    item = ItemModel.find_item(item_id)
    if item:
      try:
        item.delete_item()
      except:
        return{'message': 'An internal error ocurred while saving the item.'}, 500
      return {'message': 'Item deleted.'}
    return {'message': 'Item not found.'}, 404