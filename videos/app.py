"""
created by Nagaj at 15/06/2021
"""

from flask import Flask

from videos.api.v1 import views as v1_views
from extensions import db, migrate


def create_app():
    """
    create flaks app with configuration
    :return:
    """
    app = Flask(__name__)
    configure_db(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(v1_views.blueprint)


def configure_db(app):
    """configure flask extensions"""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    migrate.init_app(app, db)
