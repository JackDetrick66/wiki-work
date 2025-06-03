from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class user(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password_hash = db.Column(db.String(256), nullable=False)


def load_user(user_id):
    return user.query.get(int(user_id))