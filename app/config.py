import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + basedir + '/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    debug = True