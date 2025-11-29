from flask import Blueprint, render_template

bp=Blueprint('routes', __name__) #creating blueprint
#adding path to blueprint
@bp.route('/')
def index():
    return render_template('index.html') #when user goes to main page shows html web page