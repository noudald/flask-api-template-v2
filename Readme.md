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
```
