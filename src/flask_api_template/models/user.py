from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt

from flask import current_app
from sqlalchemy.ext.hybrid import hybrid_property

from flask_api_template import db, bcrypt
from flask_api_template.models.token_blacklist import BlacklistedToken
from flask_api_template.util.datetime_util import (
    utc_now,
    get_local_utcoffset,
    make_tzaware,
    localized_dt_string
)
from flask_api_template.util.result import Result


class User(db.Model):
    __tablename__ = 'site_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, default=utc_now)
    admin = db.Column(db.Boolean, default=False)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid4()))

    def __repr__(self):
        return ('<User'
                f' username={self.username}'
                f', email={self.email}'
                f', public_id={self.public_id}'
                f', admin={self.admin}'
                '>')

    @hybrid_property
    def registered_on_str(self):
        registered_on_utc = make_tzaware(
            self.registered_on, use_tz=timezone.utc, localize=False
        )
        return localized_dt_string(registered_on_utc, use_tz=get_local_utcoffset())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        log_rounds = current_app.config.get('BCRYPT_LOG_ROUNDS')
        hash_bytes = bcrypt.generate_password_hash(password, log_rounds)
        self.password_hash = hash_bytes.decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_access_token(self):
        now = datetime.now(timezone.utc)
        if current_app.config['TESTING']:
            expire = now + timedelta(seconds=1)
        else:
            token_age_h = current_app.config.get('TOKEN_EXPIRE_HOURS')
            token_age_m = current_app.config.get('TOKEN_EXPIRE_MINUTES')
            expire = now + timedelta(hours=token_age_h, minutes=token_age_m)

        payload = dict(exp=expire, iat=now, sub=self.public_id, admin=self.admin)
        key = current_app.config.get('SECRET_KEY')

        return jwt.encode(payload, key, algorithm='HS256')

    @staticmethod
    def decode_access_token(access_token):
        if isinstance(access_token, bytes):
            access_token = access_token.decode('ascii')

        if access_token.startswith('Bearer '):
            access_token = access_token.split('Bearer')[1].strip()

        try:
            key = current_app.config.get('SECRET_KEY')
            payload = jwt.decode(access_token, key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Result.Fail('Access token expired. Please login again')
        except jwt.InvalidTokenError:
            return Result.Fail('Invalid token. Please login again')

        if BlacklistedToken.check_blacklist(access_token):
            return Result.Fail('Token blacklisted. Please login again')

        user_dict = dict(
            public_id=payload['sub'],
            admin=payload['admin'],
            token=access_token,
            expires_at=payload['exp']
        )

        return Result.Ok(user_dict)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(public_id=public_id).first()

    @classmethod
    def list_all_users(cls):
        return cls.query.all()
