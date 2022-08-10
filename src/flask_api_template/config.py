'''Configuration settings for Flask API Template.'''

import os
from pathlib import Path


CUR_PATH = Path(__file__).parent

SQL_USER = os.getenv('SQL_USER')
SQL_HOST = os.getenv('SQL_HOST')
SQL_PORT = os.getenv('SQL_PORT')
SQL_DB_NAME = os.getenv('SQL_DB_NAME')
SQL_PASS = os.getenv('SQL_PASS')

SQL_DEV = f'postgresql://{SQL_USER}:{SQL_PASS}@{SQL_HOST}:{SQL_PORT}/{SQL_DB_NAME}'
SQL_TEST = 'sqlite:///flask_api_template_test.db'
SQL_PROD = 'sqlite:///flask_api_template_prod.db'


class Config:
    '''Basic configuration for Flask API'''

    APP_NAME = 'Flask API Template'
    SECRET_KEY = os.getenv('SECRET_KEY', 'NotSoSecretTestKey')
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False


class TestingConfig(Config):
    '''Testing configuration.'''

    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQL_TEST


class DevelopmentConfig(Config):
    '''Development configuration.'''

    TOKEN_EXPIRE_MINUTES = 15
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQL_DEV)


class ProductionConfig(Config):
    '''Production configuration.'''

    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQL_PROD)
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
