from sql_alchemy import db
 
class ItemModel(db.Model):
  __tablename__ = "items"

  item_id = db.Column(db.Integer, primary_key=True)
  product = db.Column(db.String())
  quantity = db.Column(db.Integer())
  price = db.Column(db.Float(precision=2))

  def __init__(self, item_id, product, quantity , price):
    self.item_id = item_id
    self.product = product
    self.quantity = quantity
    self.price = price

  def json(self):
    return {
      'item_id': self.item_id,
      'product': self.product,
      'quantity': self.quantity,
      'price': self.price
    }

  @classmethod
  def find_item(cls, item_id):
    item = cls.query.filter_by(item_id=item_id).first()
    if item:
      return item
    return None

  def find_item_all(self):
    item = self.json()
    if item:
      return item
    return None

  def save_item(self):
    db.session.add(self)
    db.session.commit()

  def update_item(self, product, quantity, price):
    self.product = product
    self.quantity = quantity
    self.price = price

  def delete_item(self):
    db.session.delete(self)
    db.session.commit()