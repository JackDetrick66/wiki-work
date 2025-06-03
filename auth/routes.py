from flask import Blueprint, request, redirect, render_template, url_for, flash, get_flashed_messages
from db_models import user, db
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp


# login route (GET)
@auth_bp.route('/login')
def login():
    return render_template('login.html')


# Signup route (GET to display form, POST to submit form)
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        raw_password = request.form['password']

        # Check if the username already exists
        existing_user = user.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken.")
            return redirect(url_for('auth.signup'))
        

        hashed_password = generate_password_hash(raw_password)
        new_user = user(username=username, password_hash=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error with commit to database:", e)
        

        flash('Signup successful!')
        return redirect(url_for('/'))

    return render_template('signup.html')