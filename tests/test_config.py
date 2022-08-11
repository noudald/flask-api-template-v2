import os

from flask_api_template import create_app
from flask_api_template.config import SQL_DEV, SQL_PROD, SQL_TEST


def test_config_development():
    app = create_app('development')
    assert app.config['SECRET_KEY'] != ''
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL', SQL_DEV)
    assert app.config['TOKEN_EXPIRE_HOURS'] == 0
    assert app.config['TOKEN_EXPIRE_MINUTES'] == 15


def test_config_testing():
    app = create_app('testing')
    assert app.config['SECRET_KEY'] != ''
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == SQL_TEST
    assert app.config['TOKEN_EXPIRE_HOURS'] == 0
    assert app.config['TOKEN_EXPIRE_MINUTES'] == 0


def test_config_production():
    app = create_app('production')
    assert app.config['SECRET_KEY'] != ''
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL', SQL_PROD)
    assert app.config['TOKEN_EXPIRE_HOURS'] == 1
    assert app.config['TOKEN_EXPIRE_MINUTES'] == 0
