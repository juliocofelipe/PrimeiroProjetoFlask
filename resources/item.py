from flask_restful import Resource, request, reqparse
from models.item import ItemModel
from sql_alchemy import db

class Items(Resource):
  def get(self):
    return {'items': [item.json() for item in ItemModel.query.all()]}

class Item(Resource):

  def get(self, item_id):
    item = ItemModel.find_item(item_id)
    if item:
      return item.json()
    return {'message': 'Item not found.'}, 404

  def post(self):
    post_data = request.get_json()
    product = post_data.get('product')
    quantity = post_data.get('quantity')
    price = post_data.get('price')
    response_object = {}
    
    if ItemModel.find_item(product):
      return {'message': "Item id {} already exists.".format(item_id)}, 400
    
    db.session.add(ItemModel(product=product, quantity=quantity, price=price))
    db.session.commit()

    response_object['message'] = f'{product} was added!'
    return response_object, 201  


  def put(self, product):
    # parser = reqparse.RequestParser()
    # parser.add_argument('product', required=True, help="The field 'Produto', cannot be left blank.")
    # parser.add_argument('quantity')
    # parser.add_argument('price')

    # data = parser.parse_args()
    # print(data)
    # try:
    data = request.get_json()
    print(data)
    #   print(data)
    #   product = ItemModel.query.filter_by(product=product).first()
    #   product = ItemModel.query.filter_by(product=product)
    #   product.update(data)
    #   db.session.commit()
    #   return jsonify(data)
    # except Exception as e:
    #     jsonify({"error":"There was an error please contact the administrator"})# Routes
   # data = Item.parser.parse_args()
   #  item_found = ItemModel.find_item(item_id)
   #  if item_found:
   #    item_found.update_item(**data)
   #    item_found.save_item()
   #    return item_found.json(), 200
   #  item = ItemModel(item_id, **data)
   #  try:
   #    item.save_item()
   #  except:
   #    return {'message': 'An internal error ocurred while saving the item.'}, 500
   #  return item.json(), 201
    
    
    item_found = ItemModel.get_by_product(product).first()
    print(item_found.product)
    if item_found:
      item_found.update_item(**data)
      item_found.save_item()
      return item_found.json(), 200
    item = ItemModel(product, **data)
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