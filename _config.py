import os

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

#define the full path for the database
DATABASE_PATH = os.path.join(basedir,DATABASE)

# the database url
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH