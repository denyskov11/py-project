from app import create_app
from app.models import db
from flask import Flask
import os

app = create_app()

if __name__ == "__main__":
    #create db tables if don't exist
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)