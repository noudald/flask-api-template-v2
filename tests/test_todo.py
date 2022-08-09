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


def list_tasks(test_client):
    return test_client.get(url_for('api.todo_tasks'))


def get_task(test_client, task_id):
    return test_client.get(url_for('api.todo_task', id=task_id))


def delete_task(test_client, access_token, task_id):
    return test_client.delete(
        url_for('api.todo_task', id=task_id),
        headers={'Authorization': f'Bearer {access_token}'}
    )

def update_task(
        test_client,
        access_token,
        task_id,
        assigned=TEST_ASSIGNED,
        task=TEST_TASK,
        deadline=TEST_DEADLINE,
        finished=TEST_FINISHED,
    ):
    return test_client.put(
        url_for('api.todo_task', id=task_id),
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

    id_ = response.json['id']
    task = TodoTask.find_by_id(id_)

    assert task.assigned == TEST_ASSIGNED
    assert task.task == TEST_TASK
    assert task.deadline.strftime('%Y-%m-%d') == TEST_DEADLINE
    assert task.finished == TEST_FINISHED

    response = get_task(client, id_)

    assert response.status_code == HTTPStatus.OK
    assert response.json['assigned'] == TEST_ASSIGNED
    assert response.json['task'] == TEST_TASK
    assert response.json['deadline'] == TEST_DEADLINE + ' 00:00:00'
    assert response.json['finished'] == TEST_FINISHED


def test_list_tasks(client):
    response = list_tasks(client)

    assert response.status_code == HTTPStatus.OK
    assert response.json['status'] == 'success'
    assert response.json['message'] == 'successfully collected all tasks'
    assert len(response.json['tasks']) > 0


def test_delete_task(client):
    response = login_user(client)

    assert response.status_code == HTTPStatus.OK

    access_token = response.json['access_token']
    response = add_task(client, access_token)

    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json

    id_ = response.json['id']

    response = delete_task(client, access_token, id_)

    assert response.status_code == HTTPStatus.NO_CONTENT

    response = get_task(client, id_)

    assert response.status_code == HTTPStatus.CONFLICT


def test_update_task(client):
    response = login_user(client)

    assert response.status_code == HTTPStatus.OK

    access_token = response.json['access_token']
    response = add_task(client, access_token)

    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json

    id_ = response.json['id']

    response = update_task(
        client,
        access_token,
        id_,
        task='This is an updated task'
    )

    assert response.status_code == HTTPStatus.ACCEPTED
    assert response.json['task'] == 'This is an updated task'
