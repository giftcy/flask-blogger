import os


class Config():
	pass


class DevelopmentConfig(Config):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'azzsacrhopyiqwa'
	DEBUG = True


class ProductionConfig(Config):
	pass


class TestingConfig(Config):
	pass


config = {
	'development':DevelopmentConfig,
	'production':ProductionConfig,
	'testing':TestingConfig,
	'default':DevelopmentConfig
}