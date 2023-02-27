import os

SECRET_KEY = os.environ.get("SECRET_KEY")
WTF_CSRF_SECRET_KEY = "a csrf secret key"
SQLALCHEMY_DATABASE_URI = 'sqlite:///cafe.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False





