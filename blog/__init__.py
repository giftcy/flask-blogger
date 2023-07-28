from flask import Flask




def create_app(config,config_class):
	app = Flask(__name__)
	app.config.from_object(config[config_class])



	return app