from datetime import datetime
from http import HTTPStatus

from flask import jsonify
from flask_restx import abort

from flask_api_template import db
from flask_api_template.models.todo import TodoTask


def new_todo_task(task, assigned, deadline, finished):
    new_task = TodoTask(
        task=task,
        assigned=assigned,
        deadline=datetime.strptime(deadline, '%d-%m-%Y'),
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

def get_todo_task(id):
    task = TodoTask.find_by_id(id)
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


def update_todo_task(id, task, assigned, deadline, finished):
    if not TodoTask.find_by_id(id):
        abort(
            HTTPStatus.CONFLICT,
            f'Task {id} does not exist.',
            status='fail'
        )

    todo_task = TodoTask.query.filter_by(id=id).first()
    todo_task.task = task
    todo_task.assigned = assigned
    todo_task.deadline = datetime.strptime(deadline, '%d-%m-%Y')
    todo_task.finished = finished
    db.session.commit()

    response = jsonify(
        status='success',
        message='successfully updated task',
        id=id,
        task=task,
        assigned=assigned,
        deadline=deadline,
        finished=finished
    )
    response.status_code = HTTPStatus.CREATED

    return response


def delete_todo_task():
    pass


def get_todo_list():
    todo_tasks = TodoTask.list_all_tasks()
    response = jsonify(
        status='succes',
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
