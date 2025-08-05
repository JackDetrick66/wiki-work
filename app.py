from flask import Flask, render_template
from flask_login import LoginManager
from db_models import db, User
from main import main_bp
from auth import auth_bp

app = Flask(__name__)

app.config.from_object('config.Config')

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

# Initialize DB
db.init_app(app)



# Set up LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# define when i want to load a users info
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contentListing')
def contentListing():
    return render_template('contentListing.html')
# will cause the app to run when its being run directly, as opposed to being imported
# debug = True should be set to false for production
if __name__ == '__main__': 
    app.run(debug=True)

