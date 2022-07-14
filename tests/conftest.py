import pytest
# import app
from app import create_app

@pytest.fixture()
def app():
    print('conftest: app fixture: before create_app()')
    local_app = create_app()
    local_app.config.update({
        "TESTING": True
    })
    print('conftest: app fixture: after app.config.update')
    
    print('conftest: app fixture: just before yield app')
    yield local_app
    print('conftest: app fixture: just after   yield app')

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def route(base, remainder):
    return f"{base}{remainder}"
