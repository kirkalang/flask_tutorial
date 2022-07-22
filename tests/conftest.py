import pytest
from typing import Dict

from tutorial.app import create_app
from tutorial.model.database import db, TEST_CONFIG
from tutorial.model import Planet, User

@pytest.fixture()
def app():
    app = create_app(TEST_CONFIG)
    app.config.update({
        "TESTING": True
    })
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def route(base, remainder):
    return f"{base}{remainder}"


@pytest.fixture
def initialize_db(app, data):
    """ Used by tests to prepopulate data into the database. 
    
    :param data: a list of dictionaries containing the table name and the data. 
    Dict format is
    {'table': 'table_name', 'field_str1': 'field1 value1', 'field_int2': 0}
    The table name indicates the table to insert data into and the field names 
    map to table columns.

    """

    with app.app_context():

        db.drop_all()
        db.create_all()

        if data['type'] == 'planet':
            for planet_dict in data['values']:
                planet = Planet(planet_dict)
                db.session.add(planet)

        elif data['type'] == 'user':
            for user_dict in data['values']:
                user = User(user_dict)
            db.session.add(user)

        db.session.commit()

    return data