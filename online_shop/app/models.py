from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #preparation for creating db

#creating table
class Product(db.Model): #creating class that describes product
    __tablename__  = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #creating product id
    #creating name
    name = db.Column(db.String(100),nullable=False) 
    price = db.Column(db.Float, nullable=False) #creating price
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    is_active  = db.Column(db.Boolean)
    category   = db.Column(db.String(50), nullable=False)
    rating  = db.Column(db.Float, nullable=True, default=0)
    sale   = db.Column(db.Boolean)
