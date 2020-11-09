import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# database connection uri
# SQLALCHEMY_DATABASE_URI = 'oracle://dbuser:april@orcl'
# STATIC_ROOT = None
