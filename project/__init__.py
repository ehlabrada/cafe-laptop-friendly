from flask import Flask

from .extensions import db
from project.routes.cafe import cafe
from project.routes.user import user
from project.routes.comment import comment


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.app_context().push()
    app.config.from_pyfile(config_file)

    db.init_app(app)
    db.create_all()

    app.register_blueprint(cafe)
    app.register_blueprint(user)
    app.register_blueprint(comment)

    return app





