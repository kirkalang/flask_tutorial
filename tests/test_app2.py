import json
import pytest

ROUTE_BASE = '/app2/'


def test_app2_helloworld(client):
    response = client.get(ROUTE_BASE)
    assert response.status_code == 200
    assert response.text == 'Hello World!'


def test_app2_supersimple(client):
    response = client.get(f'{ROUTE_BASE}super_simple')
    assert response.status_code == 200
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Hello from the Planetary API."


def test_app2_notfound(client):
    response = client.get(f'{ROUTE_BASE}not_found')

    assert response.status_code == 404