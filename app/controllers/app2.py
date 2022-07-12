"""
First excercise from the flask restful API linked in learning class
"""
from flask import Flask
from flask import Blueprint
from flask import jsonify

bp = Blueprint("app2", __name__, url_prefix="/app2")


@bp.route('/')
def hello():
    """
    Default get route that return a literal string
    """
    return 'Hello World!'


@bp.route('/super_simple')
def super_simple():
    """
    GET route that return string literal
    """
    j = jsonify(message='Hello from the Planetary API.')
    return j


@bp.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404
