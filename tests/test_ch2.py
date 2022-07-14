import json
import pytest

ROUTE_BASE = '/chap2/'

@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, '')])
def test_chap2_helloworld(client, route):
    response = client.get(route)
    assert response.status_code == 200
    assert response.text == 'Hello World!'


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'super_simple')])
def test_chap2_supersimple(client, route):
    response = client.get(route)
    assert response.status_code == 200
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Hello from the Planetary API."


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'not_found')])
def test_chap2_notfound(client, route):
    response = client.get(route)
    assert response.status_code == 404


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'parameters')])
def test_chap2_validnameisoldenough(client, route):
    response = client.get(route, query_string={'name': 'test name', 'age': 20})
    assert response.status_code == 200
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Welcome test name you are old enough!"


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'parameters')])
def test_chap2_validnamenotoldenough(client, route):
    response = client.get(route, query_string={'name': 'test name', 'age': 17})
    assert response.status_code == 401
    j = json.loads(response.data)
    assert 'message' in j.keys()
    assert j['message'] == "Sorry test name you are not old enough."


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'parameters')])
def test_chap2_validnamenoage(client, route):
    response = client.get(route, query_string={'name': 'test name'})
    assert response.status_code == 400


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'url_variables/Test/18'), (ROUTE_BASE, 'url_variables/Test/19')])
def test_chap2_urlvariables_validage(client, route):
    response = client.get(route)
    assert response.status_code == 200


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'url_variables/Test/17'), 
                                             (ROUTE_BASE, 'url_variables/Test/0')])
def test_chap2_urlvariables_invalidage(client, route):
    response = client.get(route)
    assert response.status_code == 401
