
class Config:
    ...
class ProdCofig(Config):
    ...
class DevConfig(Config):
    DEBUG = True



config_options = {
    'prod':ProdCofig,
    'dev' :DevConfig
}