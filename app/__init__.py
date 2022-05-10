from ensurepip import bootstrap
from flask import Flask
from flask_login import LoginManager
from config import config_options
from flask_bootstrap import Bootstrap

login_manager = LoginManager()


bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

