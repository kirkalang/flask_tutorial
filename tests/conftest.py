import pytest
from app import create_app

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

