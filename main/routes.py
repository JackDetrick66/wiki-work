from flask import render_template
from db_models import Article
from . import main_bp
#just returning the html
@main_bp.route('/contentListing')
def contentListing():
    # this grabs all of the articles we have, and passes it to the template
    # this is ordered by the date created, so the most recent articles are at the top
    articles = Article.query.order_by(Article.date_created.desc()).all()
    return render_template('contentListing.html', articles=articles)

@main_bp.route('/index')
def index():
    return render_template('index.html')

@main_bp.route('/view/<slug>')
def viewArticle(slug):
    # this grabs the article with the given slug, and passes it to the template
    article = Article.query.filter_by(slug=slug).first_or_404()
    return render_template('viewArticle.html', article=article)