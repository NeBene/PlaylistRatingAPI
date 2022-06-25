from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.data import *
from app.srv import *

db.create_all()