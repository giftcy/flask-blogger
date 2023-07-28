import os
from blog import create_app
from settings.config import config



app = create_app(config,os.getenv('BLOGGER_CONFIG')or 'default')


if __name__ == '__main__':
	app.run()