from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = 'Flask API Template'
APP_ROOT = Path(__file__).parent
AUTHOR = 'Noud Aldenhoven'
AUTHOR_EMAIL = 'noud.aldenhoven@gmail.com'
INSTALL_REQUIRES = [
    'Flask==2.1.2',
    'Flask-Bcrypt==1.0.1',
    'Flask-Cors==3.0.10',
    'Flask-Migrate==3.1.0',
    'Flask-SQLAlchemy==2.5.1',
    'flask-restx==0.5.1',
    'python-dotenv==0.20.0',
    'Werkzeug==2.1.2',
    'PyJWT==2.4.0',
    'python-dateutil==2.8.2',
]
EXTRAS_REQUIRE = {
    'dev': [
        'pytest==7.1.2',
        'pytest-flask==1.2.0',
        'pylint==2.14.5',
        'pylint-flask==0.6',
        'pylint-flask-sqlalchemy==0.2.0',
        'tox==3.25.1',
    ]
}

setup(
    name="flask-api-template",
    description=DESCRIPTION,
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url='https://github.com/noudald/flask-api-template-v2',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
