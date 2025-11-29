from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #preparation for creating db

#creating table
class Product(db.Model): #creating class that describes product
    __tablename__  = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #creating product id
    #creating name
    name = db.Column(db.String(100),nullable=False) 
    price = db.Column(db.Float, nullable=False) #creating price