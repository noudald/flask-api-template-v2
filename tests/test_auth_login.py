from http import HTTPStatus

from flask_api_template.models.user import User
from tests.util import USERNAME, EMAIL, register_user, login_user

SUCCESS = 'Successfully logged in'
UNAUTHORIZED = f'Username {USERNAME} does not exists'


def test_login(client, db):
    response = register_user(client)
    assert response.status_code == HTTPStatus.CREATED

    response = login_user(client)
    assert 'status' in response.json and response.json['status'] == 'success'
    assert 'message' in response.json and response.json['message'] == SUCCESS
    assert 'access_token' in response.json

    access_token = response.json['access_token']
    result = User.decode_access_token(access_token)
    assert result.success

    token_payload = result.value
    assert not token_payload['admin']

    user = User.find_by_public_id(token_payload['public_id'])
    assert user and user.email == EMAIL and user.username == USERNAME


def test_login_email_does_not_exists(client, db):
    response = login_user(client)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert ('message' in response.json and
            response.json['message'] == UNAUTHORIZED)
    assert 'access_token' not in response.json
