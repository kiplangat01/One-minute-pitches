
class Config:
    SECRET_KEY = 'python is nice'
class ProdCofig(Config):
    ...
class DevConfig(Config):
    DEBUG = True



config_options = {
    'prod':ProdCofig,
    'dev' :DevConfig
}