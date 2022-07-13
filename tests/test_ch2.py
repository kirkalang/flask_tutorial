import json
import pytest

ROUTE_BASE = '/chap2/'


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


def test_app2_validnameisoldenough(client):
    response = client.get(f'{ROUTE_BASE}parameters', query_string={'name': 'test name', 'age': 20})
    assert response.status_code == 200
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Welcome test name you are old enough!"

def test_app2_validnamenotoldenough(client):
    response = client.get(f'{ROUTE_BASE}parameters', query_string={'name': 'test name', 'age': 17})
    assert response.status_code == 401
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Sorry test name you are not old enough."

def test_app2_validnamenoage(client):
    response = client.get(f'{ROUTE_BASE}parameters', query_string={'name': 'test name'})
    assert response.status_code == 401