from flask import Flask
import os
from tutorial import model
from tutorial import controllers
from .commands import bp as commands_bp


PACKAGE_NAME = "FlaskTest"

def create_app(config_name=None):
    app = Flask( PACKAGE_NAME )

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    model.database.db.init_app(app)
    model.database.migrate.init_app(app)
    model.database.marshmallow.init_app(app)

    app.register_blueprint(controllers.chapter1_bp)
    app.register_blueprint(controllers.chapter2_bp)
    app.register_blueprint(controllers.chapter3_bp)
    app.register_blueprint(commands_bp)

    return app