"""
First excercise from the flask restful API linked in learning class
"""
from flask import Blueprint
from flask import abort, jsonify, request
from flask_marshmallow import Marshmallow
from http.client import BAD_REQUEST
import os

bp = Blueprint("chap3", __name__, url_prefix="/chap3")

from tutorial.model import User, Planet

bp.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
