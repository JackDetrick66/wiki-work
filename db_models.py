from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Chronicler(db.Model, UserMixin):
    id = d