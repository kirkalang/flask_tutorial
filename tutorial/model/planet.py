"""Contains the Planet SQLAlchemy model class and the Marshmallow PlanetSchema class.
Exposes two module level variables for utilizing PlanetSchema.
- planet_schema: for a single Planet instance
- planets_schema: for a list of Planets
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, func
from .database import db, marshmallow

class Planet(db.Model):
    """SQLAlchemy Model for Planet entities
    
    :param planet_id: Unique integer identifier for Planet. Primary Key.
    :param planet_name: String name for the planet.
    :param planet_type: String type for planet. Ex: Earth = Class M.
    :param home_star: String name of star in planet solar system.
    :param mass: Float mass of the planet.
    :param radius: Float radius of the planet in miles.
    :param distance: Float distance of planet from home_star.
    """

    __tablename__ = 'planets'
    
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


    def __init__(self, values):
        """
        :param values: dict containing values for instantiating Planet.
        Uses dict to allow test fixtures to easily initialize database 
        with specific values. The keys in the dictionary must match the
        Planet field names. A KeyError is raised if values dictionary
        is missing a required key:value pair
        """
        self.planet_name = values['planet_name']
        self.planet_type = values['planet_type']
        self.home_star = values['home_star']
        self.mass = values['mass']
        self.radius = values['radius']


    def __repr__(self) -> str:
        return f'<Planet [{self.planet_id}] {self.planet_name}>'

    @classmethod
    def get_by_name(self, name):
        """Returns Planet matching parameter name if exists in databasee
        :param name: String name of the planet matching planet_name field
        """
        return self.query.filter(func.lower(self.planet_name) == func.lower(name)).first()


class PlanetSchema(marshmallow.Schema):
    """Marshmallow Schema for Planet. Used to serialize Planet instances."""
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)