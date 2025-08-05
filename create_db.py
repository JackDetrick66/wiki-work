# create_db.py

from app import app  # the file where `app = Flask(__name__)` is defined
from db_models import db, User
from werkzeug.security import generate_password_hash

# just runs db creation
with app.app_context():
    db.create_all()
    #check if admin user exists, if not, make it :)
    print("Database created successfully.")