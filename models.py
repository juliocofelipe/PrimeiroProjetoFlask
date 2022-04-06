from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class ItemModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String())
    quantity = db.Column(db.Integer())
    price = db.Column(db.Float())
 
    def __init__(self, product, quantity , price):
        self.product = product
        self.quantity = quantity
        self.price = price