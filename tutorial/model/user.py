"""Contains the User SQLAlchemy model class and the Marshmallow PlanetSchema class.
Exposes two module level variables for utilizing UserSchema.
- user_schema: for a single User instance
- userss_schema: for a list of Userss
"""
from .database import db, marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


class User(db.Model):
    """SQLAlchemy Model for Planet entities
    
    :param id: Unique integer identifier for User. Primary Key.
    :param first_name: String user first name.
    :param last_name: String user last name
    :param email: String email.
    :param password: String passworjd.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__ (self, values):
        """
        :param values: dict containing values for instantiating User.
        Uses dict to allow test fixtures to easily initialize database 
        with specific values. The keys in the dictionary must match the
        User field names. A KeyError is raised if values dictionary
        is missing a required key:value pair
        """

        self.first_name = values['first_name']
        self.last_name = values['last_name']
        self.email = values['email']
        self.password = values['password']

    def __repr__(self) -> str:
        return f'<User [{self.id}] {self.first_name} {self.last_name}>'


class UserSchema(marshmallow.Schema):
    """Marshmallow Schema for User. Used to serialize User instances."""
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
