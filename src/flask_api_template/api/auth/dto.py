from flask_restx import inputs
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
