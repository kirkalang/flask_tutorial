from app import create_app

create_app()

# from app import app, db, migrate, model
from app.model import db, migrate
from app.commands import db_seed, db_clear