from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from models import db, ItemModel


app = Flask(__name__)
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    product = request.form['fproduct']
    quantity = request.form['fquantity']
    price = request.form['fprice']    
         
    item = ItemModel(product=product, quantity=quantity, price=price)
    db.session.add(item)
    db.session.commit()
    
  items = ItemModel.query.all()
  total = sum([item.quantity * item.price for item in items])
  return render_template('index.html', items=items, total=total)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  item = ItemModel.query.filter_by(id=id).first()
  if request.method == 'POST':
    if item:
      item.product = request.form['fproduct']
      item.quantity = request.form['fquantity']
      item.price = request.form['fprice']

      db.session.add(item)
      db.session.commit()
      return redirect('/')   
  return render_template('update.html', item=item)

@app.route('/remove/<int:id>')
def remove(id):
  item = ItemModel.query.filter_by(id=id).first()
  
  if item:
    db.session.delete(item)
    db.session.commit()
    return redirect('/')  
  return render_template('index.html', item=item)    

app.run(host='0.0.0.0', port=8080)


