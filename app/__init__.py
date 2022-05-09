from flask import Flask, render_template
from config import config_options


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import pitch
    app.register_blueprint(pitch)
    return app

