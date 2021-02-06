"""Initialize Config class to access environment variables."""
import os


class Config(object):
    """Set environment variables."""
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    API_KEY = os.getenv("API_KEY")
    AUTH_DOMAIN= os.getenv("AUTH_DOMAIN")
    DATABASE_URL=os.getenv("DATABASE_URL")
    PROJECT_ID=os.getenv("PROJECT_ID")
    STORAGE_BUCKET=os.getenv("STORAGE_BUCKET")
    MESSAGING_SENDER_ID=os.getenv("MESSAGING_SENDER_ID")
    APP_ID=os.getenv("APP_ID")
    MEASUREMENT_ID=os.getenv("MEASUREMENT_ID")
