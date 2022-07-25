from flask_restx import Model
from flask_restx import fields, inputs
from flask_restx.reqparse import RequestParser


auth_reqparser = RequestParser(bundle_errors=True)
auth_reqparser.add_argument(
    name='username',
    type=str,
    location='form',
    required=True,
    nullable=False
)
auth_reqparser.add_argument(
    name='email',
    type=inputs.email(),
    location='form',
    required=True,
    nullable=False
)
auth_reqparser.add_argument(
    name='password',
    type=str,
    location='form',
    required=True,
    nullable=False
)

user_model = Model(
    'User',
    {
        'username': fields.String,
        'email': fields.String,
        'public_id': fields.String,
        'admin': fields.Boolean,
        'registered_on': fields.String(attribute='registered_on_str'),
        'token_expires_in': fields.String,
    }
)
