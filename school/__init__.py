from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path




db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'school password'
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    with app.app_context():
        
        from . import routes
        from .model import student
        
        create_database(app)
        

        return app


def create_database(app):
    if not path.exists('school/database.db'):
        db.create_all(app=app)
        print('Created Database!')


