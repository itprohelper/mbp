import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Generic application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production environment application configuration."""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development environment application configuration."""
    DEBUG = True


class TestingConfig(Config):
    """Testing environment application configuration."""
    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4

    # Enable the TESTING flag to disable the error catching during request
    # handling so that you get better error reports when performing test
    # requests against the application.
    TESTING = True

    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

    # Disable login requirement against protected routes
    LOGIN_DISABLED = True

    # Test database connection URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
