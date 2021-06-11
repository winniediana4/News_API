from flask import Flask
from flask_bootstrap import Bootstrap
from app import main as main_blueprint

bootstrap = Bootstrap

def create_app(config_name, config_options):

 app = Flask(__name__)

 app.config.from_object(config_options[config_name])

