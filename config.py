import os


class Config:
    
    TESTING = True
    DEBUG = True
    SECRET_KEY = b'school password'
    SESSION_COOKIE_NAME = 'my_cookie'


    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://school:school@0.0.0.0:5432/school')
    SQLALCHEMY_USERNAME = 'school'
    SQLALCHEMY_PASSWORD = 'school'
    SQLALCHEMY_DATABASE_NAME = 'school'
    SQLALCHEMY_TABLE = 'student'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    JSON_SORT_KEYS = False