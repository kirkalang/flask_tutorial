"""
First excercise from the flask restful API linked in learning class
"""
from flask import Flask
from flask import Blueprint
from flask import jsonify
from flask import request

bp = Blueprint("chap2", __name__, url_prefix="/chap2")


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

@bp.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message = f"Sorry {name} you are not old enough."), 401
    else:
        return jsonify(message = f"Welcome {name} you are old enough!")


