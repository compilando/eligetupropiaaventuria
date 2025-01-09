from flask import Flask
from flasgger import Swagger
from .routes import main_blueprint
from .utils.config import swagger_config

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app, config=swagger_config)
    app.register_blueprint(main_blueprint)
    return app
