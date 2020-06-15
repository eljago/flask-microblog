from flask import Flask
from config import Config

# Creates the application object as an instance of class Flask imported from the flask package
app = Flask(__name__)
app.config.from_object(Config)

# The bottom import is a workaround to circular imports, a common problem with Flask applications.
from app import routes

