from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Creates the application object as an instance of class Flask imported from the flask package
app = Flask(__name__)
app.config.from_object(Config)

# SQLAlechemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# The bottom import is a workaround to circular imports, a common problem with Flask applications.
from app import routes, models

