#imports blueprint, and creates the auth_bp blueprint for when calling the URL_for flask method
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import routes  # Ensures routes are attached to auth_bp