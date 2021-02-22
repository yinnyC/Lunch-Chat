"""Import packages and modules for initializing our app."""
import os
from flask import Flask
from events_app.config import Config
from pyrebase import pyrebase

# Set up firebase and auth object.
firebase_config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID")
}
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Set up flask app
app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# Set up bluprint - to manage the routing
from events_app.main.routes import main
app.register_blueprint(main)
