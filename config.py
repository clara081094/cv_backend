import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    cnxCVweb = "postgresql://" \
    + os.environ.get("USER_DB") \
    + ":" \
    + os.environ.get("PASSWORD_DB") \
    + "@" \
    + os.environ.get("HOST_DB") \
    + ":" \
    + os.environ.get("PORT_DB") \
    + "/" \
    + os.environ.get("NAME_DB")

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = cnxCVweb


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True