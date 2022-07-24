from http import HTTPStatus

from flask import current_app, jsonify
from flask_restx import abort

from flask_api_template import db
from flask_api_template.models.user import User


def _get_token_expire_time():
    if current_app.config['TESTING']:
        # In Testing mode token expires in 1 second.
        return 1

    token_age_h = current_app.config.get('TOKEN_EXPIRE_HOURS')
    token_age_m = current_app.config.get('TOKEN_EXPIRE_MINUTES')
    expires_in_seconds = 3600*token_age_h + 60*token_age_m

    return expires_in_seconds


def process_registration_request(username, email, password):
    if User.find_by_username(username):
        abort(
            HTTPStatus.CONFLICT,
            f'{username} is already registered',
            status='fail'
        )
    if User.find_by_email(email):
        abort(
            HTTPStatus.CONFLICT,
            f'{email} is already registered',
            status='fail'
        )

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    access_token = new_user.encode_access_token()
    response = jsonify(
        status='success',
        message='successfully registered',
        access_token=access_token,
        token_type='bearer',
        expires_in=_get_token_expire_time()
    )
    response.status_code = HTTPStatus.CREATED
    response.headers['Cache-Control'] = 'no-store'
    response.headers['Pragma'] = 'no-cache'

    return response


def process_login_request(username, email, password):
    user_by_name = User.find_by_username(username)
    if not user_by_name:
        abort(
            HTTPStatus.UNAUTHORIZED,
            f'Username {username} does not exists',
            status='fail'
        )

    user_by_email = User.find_by_email(email)
    if not user_by_email:
        abort(
            HTTPStatus.UNAUTHORIZED,
            f'Email {email} does not exists',
            status='fail'
        )

    if user_by_name != user_by_email:
        abort(
            HTTPStatus.UNAUTHORIZED,
            f'Username {username} and email {email} do not match',
            status='fail'
        )
    user = user_by_name

    if not user.check_password(password):
        abort(
            HTTPStatus.UNAUTHORIZED,
            'Password does not match',
            status='fail'
        )

    access_token = user.encode_access_token()
    response = jsonify(
        status='success',
        message='Successfully logged in',
        access_token=access_token,
        token_type='bearer',
        expires_in=_get_token_expire_time(),
    )
    response.status_code = HTTPStatus.OK,
    response.headers['Cache-Control'] = 'no-store'
    response.headers['Pragma'] = 'no-cache'

    return response
