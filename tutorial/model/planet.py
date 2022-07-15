from .database import db, marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

    def __repr__(self) -> str:
        return f'<Planet [{self.planet_id}] {self.planet_name}>'


class PlanetSchema(marshmallow.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)