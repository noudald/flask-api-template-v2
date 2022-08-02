from datetime import datetime
from http import HTTPStatus

from flask import jsonify
from flask_restx import abort

from flask_api_template import db
from flask_api_template.models.todo import TodoTask


def new_todo_task(task, assigned, deadline, finished):
    new_task = TodoTask(
        id=id,
        task=task,
        assigned=assigned,
        deadline=deadline,
        finished=finished
    )
    db.session.add(new_task)
    db.session.commit()

    response = jsonify(
        status='success',
        message='successfully added new task',
        id=new_task.id,
        task=new_task.task,
        assigned=new_task.assigned,
        deadline=new_task.deadline,
        finished=new_task.finished
    )
    response.status_code = HTTPStatus.CREATED

    return response

def get_todo_task():
    pass


def update_todo_task():
    if not TodoTask.find_by_id(id):
        abort(
            HTTPStatus.CONFLICT,
            f'Task {id} does not exist.',
            status='fail'
        )

    new_task = TodoTask(
        id=id,
        task=task,
        assigned=assigned,
        deadline=datetime.strptime(deadline),
        finished=finished
    )
    db.session.add(new_task)
    db.session.commit()

    response = jsonify(
        status='success',
        message='successfully added new task',
        id=new_task.id,
        task=new_task.task,
        assigned=new_task.assigned,
        deadline=new_task.deadline,
        finished=new_task.finished
    )
    response.status_code = HTTPStatus.CREATED

    return response


def delete_todo_task():
    pass


def get_todo_list():
    pass
