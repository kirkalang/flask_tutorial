from .database import db, marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self) -> str:
        return f'<User [{self.id}] {self.first_name} {self.last_name}>'

class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
