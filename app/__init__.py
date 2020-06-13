from flask import Flask

# Creates the application object as an instance of class Flask imported from the flask package
app = Flask(__name__)

# The bottom import is a workaround to circular imports, a common problem with Flask applications.
from app import routes

