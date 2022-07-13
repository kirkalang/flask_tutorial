"""
First excercise from the flask restful API linked in learning class
"""
from http.client import BAD_REQUEST
#from typing_extensions import Required
from flask import Flask
from flask import Blueprint
from flask import abort, jsonify, request
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range

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

class ParametersSchema(Schema):
    name = fields.Str(
        description='The name of person whose age is being validated',
        validate=validate.Length(max=100),
        required=True)
    age = fields.Int(
        description='The integer age of name to validate.',
        validate=Range(min=0, max=200),
        required=True)


@bp.route('/parameters')
def parameters():
    try:
        result = ParametersSchema().load(request.args)
    except ValidationError as err:
        abort(BAD_REQUEST, err.messages)

    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message = f"Sorry {name} you are not old enough."), 401
    else:
        return jsonify(message = f"Welcome {name} you are old enough!")


