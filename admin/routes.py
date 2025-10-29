import datetime
from decorators import admin_required
from flask_login import current_user
from flask import render_template, request, redirect, url_for, flash
from db_models import Article, db
from . import admin_bp
from slugify import slugify


# this is to create a new article, only useable by admin roles

@admin_bp.route('/new-article', methods=['GET', 'POST'])
@admin_required 
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
            return render_template('newArticle.html')
        
        flash('Article created successfully!', 'success')
        # Redirect to the content listing page
        return redirect(url_for('main.contentListing'))
    # == 'GET' isn't required, as its the only remaining option. Leaving for clarity.
    if request.method == 'GET': 
        return render_template('newArticle.html')  
    
@admin_bp.route('/edit-article/<slug>', methods=['GET','POST'])
@admin_required
def edit_article(slug):
        article = Article.query.filter_by(slug=slug).first_or_404()

        if request.method == 'POST':
             newTitle = request.form['title']
             newBody = request.form['body']
             article.body = newBody
             article.title = newTitle
             
             article.slug = slugify(newTitle)

        try:
             #commit changes
             db.session.commit()
             flash('Article Edited Successfully!', 'success')
        except Exception as e:
             db.session.rollback()
             flash("An error occurred. Please try again.", "danger")
             print("Error with commit to database:", e)
             return redirect(render_template('editArticle.html', article=article))

        else:
             return render_template('editArticle.html', article=article)
        
@admin_required
def delete_article(slug):
     article = Article.query.filter_by(slug=slug).first_or_404()
     
     try:
        db.session.delete(article)
        db.session.commit()
        flash('Article Deleted Successfully!', 'success')
     except Exception as e:
          db.session.rollback()
          flash("an error occurred. Please try again.", "danger")
          print("error with commit to database:",e)
     
