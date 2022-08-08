import pytest

from flask_api_template import create_app
from flask_api_template import db as database
from flask_api_template.models.user import User
from tests.util import USERNAME, EMAIL, ADMIN_USERNAME, ADMIN_EMAIL, PASSWORD


@pytest.fixture
def app():
    app = create_app('testing')
    return app


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db):
    user = User(username=USERNAME, email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def admin(db):
    admin = User(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=PASSWORD,
        admin=True
    )
    db.session.add(admin)
    db.session.commit()
    return admin
