import py
from app.controllers import app2_1
from flask import Response
import json

def test_hellowowrld():
    assert app2_1.hello() == "Hello World!";

def test_supersimple():
    with app
    response = app2_1.super_simple( )
    j = json.loads(response.get_data())
    assert response.status_code == 200
    j = json.loads(response.data)
    assert j['message'] == "Hello from the Planetary API."