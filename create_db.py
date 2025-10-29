# create_db.py
import os
from app import app  # the file where `app = Flask(__name__)` is defined
from db_models import db, User
from werkzeug.security import generate_password_hash

# just runs db creation
with app.app_context():
    db.create_all()
    #check if admin user exists, if not, make it :)
    if not User.query.filter_by(username='admin').first():
        admin_password = os.environ.get('ADMIN_PASSWORD')
        if not admin_password:
            print("ERROR: ADMIN_PASSWORD environment variable not set!")
            print("Set it with: export ADMIN_PASSWORD='your-secure-password'")
            exit(1)

        admin = User(username = 'Overseer',
                    password_hash = generate_password_hash(admin_password),
                    role='admin',
                    is_admin=True)
        # add the admin user to the database
        db.session.add(admin)
        db.session.commit()
        print("Admin user created. YIPPEE")
    else:
        print(r"Admin user already present \_(0_0)_/")
    print("Database created successfully.")