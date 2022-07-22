import json
import os

from flask import Blueprint
from flask import abort, jsonify, request
from flask_marshmallow import Marshmallow
from tutorial.model import User, Planet, planets_schema, planet_schema, users_schema


bp = Blueprint("chap3", __name__, url_prefix="/chap3")


@bp.route('/planets', methods=['GET'])
def planets():
    """GET route to retrieve all planet rows from the database
       :return: json list of planets with each planet represented as json dictionary
    """
    planets_list = Planet.query.all()
    response = planets_schema.dump(planets_list)
    return jsonify(response)


@bp.route('/planet/<string:name>', methods=['GET'])
def planet_with_name(name: str):
    """GET route to retrieve a planet using 'name' in URL
       :return: json dictionary representation of planet
    """
    planet_by_name = Planet.get_by_name(name)
    return jsonify( planet_schema.dump(planet_by_name) )


@bp.route('/users', methods=['GET'])
def users():
    """GET route to retrieve all users from the database
       :return: json list of users with each user represented as json dictionary
    """
    users = User.query.all()
    response = users_schema.dump(users)
    return jsonify(response)