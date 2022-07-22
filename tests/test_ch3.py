import json
import pytest

ROUTE_BASE = '/chap3/'

@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'planets')])
@pytest.mark.parametrize('data', [
    {'type': 'planet', 'values': [{'planet_name': 'Mercury',
                                   'planet_type': 'Class D',
                                   'home_star': 'Sol',
                                   'mass': 3.258e23,
                                   'radius': 1516,
                                   'distance': 35.98e6},
                                  {'planet_name': 'Venus',
                                   'planet_type': 'Class K',
                                   'home_star': 'Sol',
                                   'mass' : 4.867e24,
                                   'radius' : 3760,
                                   'distance' : 67.24e6},
                                  {'planet_name' : 'Earth',
                                   'planet_type' : 'Class M',
                                   'home_star' : 'Sol',
                                   'mass' : 5.972e24,
                                   'radius' : 3959,
                                   'distance' : 92.96e6}]
    }])
def test_chap3_get_planets(client, route, initialize_db):
    response = client.get(route)
    assert response.status_code == 200
    planets = json.loads(response.data)
    assert len(planets) == 3


@pytest.mark.parametrize('base, remainder', [(ROUTE_BASE, 'users')])
@pytest.mark.parametrize('data', [
    {'type': 'user', 'values': [{'first_name': 'William',
                                 'last_name': 'Herschel',
                                 'email': 'test@test.com',
                                 'password': 'P@ssw0rd'}]
    }])
def test_chap3_get_users(client, route, initialize_db):
    response = client.get(route)
    assert response.status_code == 200
    planets = json.loads(response.data)
    assert len(planets) == 1
