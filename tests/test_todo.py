from datetime import date
from http import HTTPStatus

from flask import url_for

from flask_api_template.models.todo import TodoTask

from tests.util import login_user


TEST_ASSIGNED = 'Noud'
TEST_TASK = 'This is a test task'
TEST_DEADLINE = date.today().strftime('%Y-%m-%d')
TEST_FINISHED = False


def add_task(
        test_client,
        access_token,
        assigned=TEST_ASSIGNED,
        task=TEST_TASK,
        deadline=TEST_DEADLINE,
        finished=TEST_FINISHED,
    ):
    return test_client.post(
        url_for('api.todo_tasks'),
        data=f'assigned={assigned}&task={task}&deadline={deadline}&finished={str(finished).lower()}',
        content_type='application/x-www-form-urlencoded',
        headers={'Authorization': f'Bearer {access_token}'}
    )


def test_add_task(client):
    response = login_user(client)

    assert response.status_code == HTTPStatus.OK

    response = add_task(client, response.json['access_token'])

    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json

    task = TodoTask.find_by_id(response.json['id'])

    assert task.assigned == TEST_ASSIGNED
    assert task.task == TEST_TASK
    assert task.deadline.strftime('%Y-%m-%d') == TEST_DEADLINE
    assert task.finished == TEST_FINISHED
