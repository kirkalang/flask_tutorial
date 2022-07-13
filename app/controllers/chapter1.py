"""
First excercise from the flask restful API linked in learning class
"""
from flask import Blueprint

bp = Blueprint("chap1", __name__, url_prefix="/chap1")

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
    return 'Hello from the Planetary API.'
