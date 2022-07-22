from flask import Flask
from flask import Blueprint
from flask import abort, jsonify, request
from http.client import BAD_REQUEST
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range


bp = Blueprint("chap2", __name__, url_prefix="/chap2")


@bp.route('/super_simple')
def super_simple():
    """GET route that returns json response with message field"""
    j = jsonify(message='Hello from the Planetary API.')
    return j


@bp.route('/not_found')
def not_found():
    """GET route to return 404 and a json response with message field"""
    return jsonify(message='That resource was not found'), 404


class ParametersSchema(Schema):
    """Marshmallow schema used to validate request args"""

    name = fields.Str(
        metadata = {'description': 'The name of person whose age is being validated'},
        validate=validate.Length(max=100),
        required=True)
    
    age = fields.Int(
        metadata = {'description': 'The integer age of name to validate.'},
        validate=Range(min=0, max=200),
        required=True)


@bp.route('/parameters')
def parameters():
    """GET route that requires 2 URL parameters: name and age 
    
        :return: 200 and success message if age >= 18, otherwise 401 and error message
    """
    try:
        result = ParametersSchema().load(request.args)
    except ValidationError as err:
        abort(BAD_REQUEST, '\n'.join([f"{i} : {err.messages[i]}" for i in err.messages.keys()]))

    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message = f"Sorry {name} you are not old enough."), 401
    else:
        return jsonify(message = f"Welcome {name} you are old enough!")


@bp.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    """GET route that uses URL variables instead of parameters

       :return: 200 and success message if age >= 18, otherwise 401 and error message
    """
    if age < 18:
        return jsonify(message = f"Sorry {name} you are not old enough."), 401
    else:
        return jsonify(message = f"Welcome {name} you are old enough!")
 
