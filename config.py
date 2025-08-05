import os

class Config:
    # secret key is needed to make sure we dont store passwords in plaintext
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-fallback-secret"
    # set the database we're using
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False