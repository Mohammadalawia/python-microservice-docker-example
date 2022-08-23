import os


class Config:

    TESTING = True
    DEBUG = True
    SECRET_KEY = b'school password'
    SESSION_COOKIE_NAME = 'my_cookie'


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://school:school@db:5432/school'
    SQLALCHEMY_BINDS = {
        'school2' :                'postgresql+psycopg2://school:school@db:5432/school2'
        }
  
    SQLALCHEMY_USERNAME = 'school'
    SQLALCHEMY_PASSWORD = 'school'
    SQLALCHEMY_DATABASE_NAME = 'school'
    SQLALCHEMY_TABLE = 'student'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    JSON_SORT_KEYS = False