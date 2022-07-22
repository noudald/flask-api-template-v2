from flask import Blueprint
from flask_restx import Api

from flask_api_template.api.auth.endpoints import auth_ns

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
    }
}

api = Api(
    api_bp,
    version='1.0',
    title='Flask API template with JWT-Based Authorization',
    description='Welcome to the Swagger UI documentation',
    doc='/ui/',
    authorizations=authorizations,
)

api.add_namespace(auth_ns, path='/auth')
