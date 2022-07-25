import os

from flask_api_template import create_app, db
from flask_api_template.models.token_blacklist import BlacklistedToken
from flask_api_template.models.user import User

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def shell():
    return {
        'db': db,
        'BlacklistedToken': BlacklistedToken,
        'User': User,
    }
