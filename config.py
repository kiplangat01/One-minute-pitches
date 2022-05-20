import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


class Config:
     SECRET_KEY = 'python is nice'
    
class ProdCofig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://moringa:bca321@localhost:5432/addpitch'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    DEBUG = True



config_options = {
    'prod':ProdCofig,
    'dev' :DevConfig
}