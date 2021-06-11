from config import DevConfig
from flask import Flask
from flask_bootstrap import Bootstrap
from app import main as main_blueprint
from .requests import configure_request


bootstrap = Bootstrap

def create_app(config_name, config_options):

 app = Flask(__name__)

 app.config.from_object(config_options[config_name])

 app = Flask(__name__, instance_relative_config = True)

 app.config.from_object(DevConfig)
 app.config.from_pyfile('config.py')

 bootstrap.init_app(app)

 app.register_blueprint(main_blueprint)

 configure_request(app)