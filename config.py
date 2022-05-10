import os
from dotenv import load_dotenv

load_dotenv()


class Config:
     SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdCofig(Config):


    ...
class DevConfig(Config):
    DATABASE_URL = os.environ.get('DEV_DATABASE_URL')
    
    DEBUG = True



config_options = {
    'prod':ProdCofig,
    'dev' :DevConfig
}