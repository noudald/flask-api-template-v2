from functools import wraps

from flask import request
from werkzeug.exceptions import Forbidden, Unauthorized

from flask_api_template.models.user import User


def _check_access_token():
    token = request.headers.get('Authorization')

    if not token:
        raise Unauthorized()

    result = User.decode_access_token(token)
    if result.failure:
        raise Unauthorized()

    return result.value


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token()

        for name, val in token_payload.items():
            setattr(decorated, name, val)

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token()

        if not token_payload['admin']:
            raise Forbidden()

        for name, val in token_payload.items():
            setattr(decorated, name, val)

        return f(*args, **kwargs)

    return decorated
