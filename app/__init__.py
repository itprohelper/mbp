import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from dotenv import load_dotenv

basedir = os.path.join(os.path.dirname(__file__), '..')
load_dotenv(os.path.join(basedir, '.env'))

app_config = os.environ['APP_SETTINGS']

if os.name == 'nt':
    app_config = app_config.replace("'", "")

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'


def create_app(config_class=app_config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.mbp import bp as mbp_bp
    app.register_blueprint(mbp_bp, url_prefix='/mbp')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
