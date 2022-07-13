import pytest


def test_helloworld(client):
    response = client.get('/chap1/')
    assert response.status_code == 200
    assert response.text == 'Hello World!'
    # j = json.loads(response.data)
    # assert j['message'] == "Hello world!"