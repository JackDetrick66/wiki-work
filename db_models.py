from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()
# create the User class for the database, with id, username, and password_hash columns
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    role = db.Column(db.String(150), default="Observer")
    is_admin = db.Column(db.Boolean, default=False)
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique = True, nullable = False)
    body = db.Column(db.Text(), nullable = False)
    last_modified = db.Column(db.DateTime, default = func.now(), onupdate=func.now())
    date_created = db.Column(db.DateTime, default = func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    creator = db.relationship('User', backref='articles')
    slug = db.Column(db.String(200), unique=True, nullable = False)



def __repr__(self):
    return f'<User {self.username}>'