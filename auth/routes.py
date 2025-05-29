from flask import render_template

from . import auth_bp

@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')
#make login