from tutorial import create_app

create_app()

# from app import app, db, migrate, model
from tutorial.model import db, migrate
from tutorial.commands import db_seed, db_clear