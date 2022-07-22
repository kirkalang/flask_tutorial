import os
from flask import Flask
from tutorial import controllers
from tutorial.model import configure_database
from .commands import bp as commands_bp


PACKAGE_NAME = 'FlaskTest'


def create_app(config_name=None):
    """Instantiates the Flask app and the SQLAlchemy database
    and associated extensions. 
    Registers the various Flask Blueprints. Using Blueprint avoid having
    to expose the Flask app as a global variable and circular dependencies
    
    :param config_name: Primarilly used to specify the Test configuration
    """
    
    app = Flask( PACKAGE_NAME )

    with app.app_context():
        configure_database(app, config_name)
    
    app.register_blueprint(controllers.chapter1_bp)
    app.register_blueprint(controllers.chapter2_bp)
    app.register_blueprint(controllers.chapter3_bp)
    app.register_blueprint(commands_bp)

    return app