from flask_restful import Resource, request
from models.item import ItemModel

class Items(Resource):
  def get(self):
    return [item.json() for item in ItemModel.query.all()]

class Item(Resource):

  def get(self, item_id):
    item = ItemModel.find_item(item_id)
    if item:
      return item.json()
    return {'message': 'Item not found.'}, 404

  def post(self):
    post_data = request.get_json()
    name = post_data.get('name')
    quantity = post_data.get('quantity')
    price = post_data.get('price')
    response_object = {}

    item = ItemModel(name=name, quantity=quantity, price=price)
    item.save_item()

    response_object['message'] = f'{name} was added!'
    return response_object, 201  


  def put(self, item_id):
    data = request.get_json()
    item = ItemModel.find_item(item_id)
    response_object = {}
    
    if item:
      item.update_item(**data)
      item.save_item()
      response_object['message'] = f'{item_id} was updated!'
      return response_object, 204
      
    response_object['message'] = f'{item_id} was not found!'
    return response_object, 404
    
  
  def delete(self, item_id):
    item = ItemModel.find_item(item_id)
    if item:
      try:
        item.delete_item()
      except:
        return{'message': 'An internal error ocurred while saving the item.'}, 500
      return {'message': 'Item deleted.'}
    return {'message': 'Item not found.'}, 404