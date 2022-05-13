from ensurepip import bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config_options
from flask_mail import Mail
from flask_bootstrap import Bootstrap

login_manager = LoginManager()


mail = Mail()
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)   
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

