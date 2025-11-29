from flask import Flask
import json
import os
def create_app():
    base_dir=os.path.abspath(os.path.dirname(__file__)+ '/..') #searching the main folder and converting it to absolute path
    app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'), #where to search tamplates such as css and js
                static_folder=os.path.join(base_dir, 'static'))
     # Load config from JSON file
    config_path = os.path.join(base_dir, 'config.json') #searching json file
    with open(config_path) as f:
        config = json.load(f)
    app.config.update(config) #add all config information to FLASK
    # Set up SQLAlchemy with absolute DB path
    db_path = os.path.abspath(os.path.join(base_dir, config['DB_PATH']))
    # Ensure the DB directory exists so SQLite can create the file
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir): 
        os.makedirs(db_dir, exist_ok=True) #if theres no folder creating one
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}" #where is our db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turning off anoying messages
    #connecting models
    from .models import db #importing db from models
    db.init_app(app) #connecting db with Flask
    #registering routes and blueprint
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    return app