""" Primary entry point for the Tutorial Flask app.
Calls the create_app function to instantiate and configure the Flask app
"""
from tutorial import create_app
create_app()

# Placed here to avoid circular imports
from tutorial.commands import db_create, db_clear, db_seed