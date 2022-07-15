import pytest
# import app
from tutorial.app import create_app

@pytest.fixture()
def app():
    print('conftest: app fixture: before create_app()')
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    print('conftest: app fixture: after app.config.update')
    
    print('conftest: app fixture: just before yield app')
    yield app
    print('conftest: app fixture: just after   yield app')

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def route(base, remainder):
    return f"{base}{remainder}"
