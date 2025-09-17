from decorators import admin_required
from flask_login import current_user
from flask import render_template, request, redirect, url_for, flash
from db_models import Article, db
from . import admin_bp
from slugify import slugify


# this is to create a new article, only useable by admin roles
@admin_required 
@admin_bp.route('/new-article', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        # Handle form submission for creating a new article
        title = request.form['title']
        content = request.form['body']
        creator = current_user.id
        slug_info = slugify(title)
        new_article = Article(title = title, body = content, created_by = creator, slug = slug_info)
        try:
        # add this article to the database
            db.session.add(new_article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash("An error occurred. Please try again.", "danger")
            print("Error with commit to database:", e)
        
        flash('Article created successfully!', 'success')
        # Redirect to the content listing page
        return redirect(url_for('main.contentListing'))
    if request.method == 'GET':
        return render_template('newArticle.html')  
    
