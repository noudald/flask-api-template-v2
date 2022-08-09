from http import HTTPStatus

from flask import jsonify
from flask_restx import abort

from flask_api_template import db
from flask_api_template.api.auth.decorators import token_required
from flask_api_template.models.todo import TodoTask


@token_required
def new_todo_task(task, assigned, deadline, finished):
    new_task = TodoTask(
        task=task,
        assigned=assigned,
        deadline=deadline,
        finished=finished
    )
    db.session.add(new_task)
    db.session.commit()

    return dict(
            id=new_task.id,
            task=new_task.task,
            assigned=new_task.assigned,
            deadline=new_task.deadline,
            finished=new_task.finished,
        ), HTTPStatus.CREATED


def get_todo_task(id_):
    task = TodoTask.find_by_id(id_)
    if not task:
        abort(
            HTTPStatus.CONFLICT,
            f'Task {id} does not exist.',
            status='fail'
        )

    return dict(
            id=task.id,
            assigned=task.assigned,
            task=task.task,
            deadline=task.deadline,
            finished=task.finished,
        ), HTTPStatus.OK


@token_required
def update_todo_task(id_, task, assigned, deadline, finished):
    if not TodoTask.find_by_id(id_):
        abort(
            HTTPStatus.CONFLICT,
            f'Task {id} does not exist.',
            status='fail'
        )

    todo_task = TodoTask.query.filter_by(id=id_).first()
    todo_task.task = task
    todo_task.assigned = assigned
    todo_task.deadline = deadline
    todo_task.finished = finished
    db.session.commit()

    response = dict(
        id=id_,
        task=task,
        assigned=assigned,
        deadline=deadline,
        finished=finished
    )

    return response, HTTPStatus.ACCEPTED


@token_required
def delete_todo_task(id_):
    task = TodoTask.find_by_id(id_)
    if not task:
        abort(
            HTTPStatus.CONFLICT,
            f'Task {id} does not exist.',
            status='fail'
        )

    db.session.delete(task)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT


def get_todo_list():
    todo_tasks = TodoTask.list_all_tasks()
    response = jsonify(
        status='success',
        message='successfully collected all tasks',
        tasks=[
            {
                'id': task.id,
                'task': task.task,
                'assigned': task.assigned,
                'deadline': task.deadline,
                'finished': task.finished
            } for task in todo_tasks
        ],
    )

    return response
