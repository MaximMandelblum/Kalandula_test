from flask import Flask

from pathlib import Path

APP_ROOT_PATH = Path(__file__).parent


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')


    with app.app_context():
        from . import routes

        return app
