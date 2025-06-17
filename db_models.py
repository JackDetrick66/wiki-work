from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
# create the User class for the database, with id, username, and password_hash columns
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password_hash = db.Column(db.String(256), nullable=False)

# define when i want to load a users info
def load_user(user_id):
    return User.query.get(int(user_id))