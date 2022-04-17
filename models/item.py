from sql_alchemy import db
 
class ItemModel(db.Model):
  __tablename__ = "items"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  quantity = db.Column(db.Integer())
  price = db.Column(db.Float(precision=2))

  def __init__(self, name, quantity , price):
    self.name = name
    self.quantity = quantity
    self.price = price

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'quantity': self.quantity,
      'price': self.price
    }

  @classmethod
  def get_by_product(cls, name):
    return cls.query.filter_by(name=name)

  @classmethod
  def find_item(cls, item_id):
    item = cls.query.filter_by(id=item_id).first()
    if item:
      return item
    return None

  def save_item(self):
    db.session.add(self)
    db.session.commit()

  def update_item(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price

  def delete_item(self):
    db.session.delete(self)
    db.session.commit()