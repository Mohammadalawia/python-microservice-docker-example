from flask import Flask
from flask_sqlalchemy import SQLAlchemy 





db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # app.config['SECRET_KEY'] = 'school password'
    # app.config['JSON_SORT_KEYS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://school:school@172.30.0.3:5432/school' #keeps changing 
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
    #                                          'postgresql+psycopg2://school:school@0.0.0.0:5432/school')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    with app.app_context():
        
        from . import routes
        from .model import student

        return app


# def create_database(app):
#     if not path.exists('/school.db'):
#         db.create_all(app=app)
#         print('Created Database!')


