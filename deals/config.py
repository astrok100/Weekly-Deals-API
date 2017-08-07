import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    MONGO_DATABASE_URI = 'mongodb://localhost:27017/'
    MONGO_DATABASE = 'Deals'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'bookshelf.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_CONFIRMABLE = False
    CACHE_TYPE = 'simple'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    MONGO_DATABASE_URI = 'mongodb://localhost:27017/'
    MONGO_DATABASE = 'Deals'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    MONGO_DATABASE_URI = 'mongodb://localhost:27017/'
    MONGO_DATABASE = 'Deals'
