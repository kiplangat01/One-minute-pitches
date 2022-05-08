from flask import Flask 


def create_app():
    app = Flask(__name__)
    from .main import pitch
    app.register_blueprint(pitch)
    return app
