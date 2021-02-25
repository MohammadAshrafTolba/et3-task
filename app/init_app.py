"""
This file is responsible for initializing app components
"""

from flask import Flask
from flask_restful import Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)
#api = Api(app)
app.config.from_object(Config)
ma = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models