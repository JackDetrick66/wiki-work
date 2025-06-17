from flask import Blueprint

# initializes the main_bp blueprint for the URL_for method
main_bp = Blueprint('main', __name__, url_prefix='/main')

from . import routes
