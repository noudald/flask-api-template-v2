from http import HTTPStatus

from flask_restx import Namespace, Resource

from flask_api_template.api.auth.dto import auth_reqparser
from flask_api_template.api.auth.business import process_registration_request

auth_ns = Namespace(name='auth', validate=True)


@auth_ns.route('/register', endpoint='auth_register')
class RegisterUser(Resource):
    @auth_ns.expect(auth_reqparser)
    @auth_ns.response(
        int(HTTPStatus.CREATED),
        'New user was successfully created.'
    )
    @auth_ns.response(
        int(HTTPStatus.CONFLICT),
        'Username or email address is already taken.'
    )
    @auth_ns.response(
        int(HTTPStatus.BAD_REQUEST),
        'Validation error.'
    )
    @auth_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    def post(self):
        request_data = auth_reqparser.parse_args()

        username = request_data.get('username')
        email = request_data.get('email')
        password = request_data.get('password')

        return process_registration_request(username, email, password)
