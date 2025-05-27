# app.py
from flask import Flask, render_template
from main import main_bp
from auth import auth_bp


app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contentListing')
def contentListing():
    return render_template('contentListing.html')

if __name__=='__main__': 
   app.run(debug=True) 

