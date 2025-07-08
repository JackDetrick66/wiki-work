from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()
# create the User class for the database, with id, username, and password_hash columns
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)


def __repr__(self):
    return f'<User {self.username}>'