import os

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, upgrade
from tutorial import model


DB_FILE_NAME = 'planets.db'
TEST_CONFIG = 'test'


db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def configure_database(app, config_name=None):
    """Configures the local sqlite database and SqlAlchemy model. 
       :param app: the Flask app. Used to initialize SQLAlchemy, Migrate & Marshmallow
       :param config_name: Primarilly used for testing to use test specific Db and init the test Db
    """
    test_config = config_name is not None and config_name == TEST_CONFIG
    db_file = DB_FILE_NAME

    if (test_config):
        db_file = TEST_CONFIG + db_file

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_file)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    model.database.db.init_app(app)
    model.database.migrate.init_app(app)
    model.database.marshmallow.init_app(app)

