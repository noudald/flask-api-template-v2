# Flask API Template

A template for Flask APIs.

# Install

## Locally

Create a new virtual environment
```
python -m venv venv --prompt flask-api-template
source venv/bin/activate
```

After activating the virtual environment upgrade pip, setuptools, and wheel
```
pip install --upgrade pip setuptools wheel
```

Create a file `.env` in the root folder with
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY="Change the secret key"
SQL_USER="Database user"
SQL_HOST="Database hostname"
SQL_PORT="Database port"
SQL_DB_NAME="Database name"
SQL_PASS="Database password"
```

To run the unit tests and linter:
```
pip install -e ".[dev]"
tox
```
