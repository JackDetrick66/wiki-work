# create_db.py

from app import app  # the file where `app = Flask(__name__)` is defined
from db_models import db
# just runs db creation
with app.app_context():
    db.create_all()
    print("Database created successfully.")