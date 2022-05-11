import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


class Config:
     SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdCofig(Config):


    ...
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    
    DEBUG = True



config_options = {
    'prod':ProdCofig,
    'dev' :DevConfig
}