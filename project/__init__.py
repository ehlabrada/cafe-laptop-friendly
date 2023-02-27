from flask import Flask
from flask_migrate import Migrate


from .extensions import db, login_manager
from project.routes.cafe_view import cafe
from project.routes.user_view import user
from project.routes.comment_view import comment

from dotenv import load_dotenv

load_dotenv


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.app_context().push()
    app.config.from_pyfile(config_file)
    app.config['SECRET_KEY']

    db.init_app(app)
    db.create_all()
    # login_manager.login_view = 'user.login'
    login_manager.init_app(app)

    app.register_blueprint(cafe)
    app.register_blueprint(user)
    app.register_blueprint(comment)

    return app





