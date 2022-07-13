from flask import Flask
from app.controllers import chapter1, chapter2

PACKAGE_NAME = "FlaskTest"
def create_app(config_name=None):
    app = Flask( PACKAGE_NAME )
    app.register_blueprint(chapter1.bp)
    app.register_blueprint(chapter2.bp)
    return app