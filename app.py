from flask import Flask, render_template
from flask_login import LoginManager
from db_models import db, load_user, User
from main import main_bp
from auth import auth_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'some-secure-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

# Initialize DB
db.init_app(app)

# Set up LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.user_loader(load_user)  # use imported load_user

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contentListing')
def contentListing():
    return render_template('contentListing.html')

if __name__ == '__main__': 
    app.run(debug=True)

