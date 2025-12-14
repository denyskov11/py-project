from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product #impotring class db and class Product

bp=Blueprint('routes', __name__) #creating blueprint
#adding path to blueprint
@bp.route('/')
def index():
    return render_template('index.html') #when user goes to main page shows html web page
@bp.route('/products')
def product():
    products=Product.query.all()
    return render_template('product_list.html', products=products)
@bp.route('/add', methods=['GET', 'POST']) #if someone goes to /add return data from the form
def add_product():
     if request.method == 'POST': #if user clicked button in the form
        name = request.form['name']#what user wrote in the name field
        price = request.form['price'] #what user wrote in the price field
        description = request.form['description'] 
        stock = request.form['stock']
        is_active = request.form.get('is_active') == 'on'
        category = request.form['category']
        rating = request.form['rating']
        sale = request.form.get('sale') == 'on'
        product = Product(name=name, price=float(price), description=description, stock=float(stock), is_active=is_active, category=category, rating=float(rating), sale=sale) #creating new product, converting some data to nubmer format
        db.session.add(product)
        db.session.commit()  #adding created product to the db
        flash('Product added!')
        return redirect(url_for('routes.product')) #back to the product list page
     return render_template('product_form.html', action='Add', product=None) #if user did not submit form, showing html form