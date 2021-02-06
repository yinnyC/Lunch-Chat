"""Import packages and modules for initializing our app."""

from flask import Flask
from events_app.config import Config

app = Flask(__name__)
app.config.from_object(Config) 

from events_app.main.routes import main
app.register_blueprint(main)