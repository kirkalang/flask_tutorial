from flask import Flask
from app.controllers import app1, app2

PACKAGE_NAME = "FlaskTest"
def create_app(config_name=None):
    app = Flask( PACKAGE_NAME )
    app.register_blueprint(app1.bp)
    app.register_blueprint(app2.bp)
    return app