"""Initialize Config class to access environment variables."""
import os


class Config(object):
    """Set environment variables."""
    SECRET_KEY = os.getenv("SECRET_KEY")