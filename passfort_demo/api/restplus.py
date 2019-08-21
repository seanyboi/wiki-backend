import traceback

from flask_restplus import Api
from passfort_demo import settings
from sqlalchemy.orm.exc import NoResultFound

api = Api(version='1.0', title='PassFort Documentation Wikipedia',
          description='Demonstration of a Flask API')


# Defines universal errors to be used within swagger applicaiton
@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404
