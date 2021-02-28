"""App configuration."""
from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    DB_REGIONS = ['us-east-1', 'us-east-2', 'eu-west-1']