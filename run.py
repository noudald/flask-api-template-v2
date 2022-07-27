import os

import click

from flask_api_template import create_app, db
from flask_api_template.models.token_blacklist import BlacklistedToken
from flask_api_template.models.user import User
from flask_api_template.models.todo import TodoTask

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def shell():
    return {
        'db': db,
        'BlacklistedToken': BlacklistedToken,
        'User': User,
        'TodoTask': TodoTask,
    }


@app.cli.command('add-user', short_help='Add new user')
@click.argument('username')
@click.argument('email')
@click.option(
    '--admin',
    is_flag=True,
    default=False,
    help='New user has administrator privilages'
)
@click.password_option(help='Do not set password on the command line!')
def add_user(username, email, password, admin):
    if User.find_by_username(username):
        click.secho(
            f'Error: Username {username} has already been taken.',
            fg='red',
            bold=True
        )

        return 1

    if User.find_by_email(email):
        click.secho(
            f'Error: Email {email} has already been taken.',
            fg='red',
            bold=True
        )

        return 1

    new_user = User(
        username=username,
        email=email,
        password=password,
        admin=admin
    )
    db.session.add(new_user)
    db.session.commit()

    if admin:
        click.secho(
            f'Successfully added new admin user: {username}',
            fg='blue',
            bold=True
        )
    else:
        click.secho(
            f'Successfully added new user: {username}',
            fg='blue',
            bold=True
        )

    return 0


@app.cli.command('list-users', short_help='List all users')
def list_users():
    print('List of users:')
    for user in User.list_all_users():
        print(user)

    return 0
