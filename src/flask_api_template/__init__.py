from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_api_template.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    config = get_config(config_name)
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    # Import in function to avoid circular imports.
    # pylint: disable=import-outside-toplevel,cyclic-import
    from flask_api_template.api import api_bp
    app.register_blueprint(api_bp)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app
