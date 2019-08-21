import os
from flask import Flask, Blueprint
from passfort_demo import settings
from passfort_demo.api.wiki.endpoints.titles import ns as wiki_titles_namespace
from passfort_demo.api.restplus import api
from passfort_demo.database import db

app = Flask(__name__)

# set basic configurations
def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

# define initialisation and blueprint of application
def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(wiki_titles_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)

# initialises and runs the application
def main():
    initialize_app(app)
    app.run()


if __name__ == "__main__":
    main()
