# We have to use id for identification number of todo task.
# pylint: disable=redefined-builtin

from http import HTTPStatus

from flask_restx import Namespace, Resource

from flask_api_template.api.todo.dto import (
    todo_reqparser,
    todo_model,
    todo_list_model,
)
from flask_api_template.api.todo.business import (
    new_todo_task,
    update_todo_task,
    get_todo_task,
    delete_todo_task,
    get_todo_list
)


todo_ns = Namespace(name='todo', validate=True)
todo_ns.models[todo_model.name] = todo_model
todo_ns.models[todo_list_model.name] = todo_list_model


@todo_ns.route('/task', endpoint='todo_tasks')
class TodoList(Resource):
    @todo_ns.doc(security='Bearer')
    @todo_ns.expect(todo_reqparser)
    @todo_ns.response(
        int(HTTPStatus.CREATED),
        'New task was successfully create.'
    )
    @todo_ns.response(
        int(HTTPStatus.BAD_REQUEST),
        'Validation error.'
    )
    @todo_ns.response(
        int(HTTPStatus.UNAUTHORIZED),
        'You do not have permission to add a new task.'
    )
    @todo_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    @todo_ns.marshal_with(todo_model)
    def post(self):
        '''Add new task to todo list.'''
        request_data = todo_reqparser.parse_args()

        task = request_data.get('task')
        assigned = request_data.get('assigned')
        deadline = request_data.get('deadline')
        finished = request_data.get('finished')

        return new_todo_task(task, assigned, deadline, finished)

    @todo_ns.response(
        int(HTTPStatus.OK),
        'Succesfully collected all tasks.',
        todo_list_model
    )
    @todo_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    def get(self):
        '''Get list of all todo list tasks.'''
        return get_todo_list()


@todo_ns.route('/task/<int:id>', endpoint='todo_task')
class TodoTask(Resource):
    @todo_ns.doc(security='Bearer')
    @todo_ns.expect(todo_reqparser)
    @todo_ns.response(
        int(HTTPStatus.ACCEPTED),
        'Successfully updated task.',
        todo_model
    )
    @todo_ns.response(
        int(HTTPStatus.NOT_FOUND),
        'Task not found. Id incorrect.'
    )
    @todo_ns.response(
        int(HTTPStatus.BAD_REQUEST),
        'Validation error.'
    )
    @todo_ns.response(
        int(HTTPStatus.UNAUTHORIZED),
        'You do not have permission to update a task.'
    )
    @todo_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    @todo_ns.marshal_with(todo_model)
    def put(self, id):
        '''Update todo tasks.'''
        request_data = todo_reqparser.parse_args()

        task = request_data.get('task')
        assigned = request_data.get('assigned')
        deadline = request_data.get('deadline')
        finished = request_data.get('finished')

        return update_todo_task(id, task, assigned, deadline, finished)

    @todo_ns.response(
        int(HTTPStatus.OK),
        'Successfully retrieved task.',
        todo_model
    )
    @todo_ns.response(
        int(HTTPStatus.NOT_FOUND),
        'Task not found. Id incorrect.'
    )
    @todo_ns.response(
        int(HTTPStatus.BAD_REQUEST),
        'Validation error.'
    )
    @todo_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    @todo_ns.marshal_with(todo_model)
    def get(self, id):
        '''Get todo task.'''
        return get_todo_task(id)

    @todo_ns.doc(security='Bearer')
    @todo_ns.response(
        int(HTTPStatus.NO_CONTENT),
        'Successfully deleted task.'
    )
    @todo_ns.response(
        int(HTTPStatus.NOT_FOUND),
        'Task not found. Id incorrect.'
    )
    @todo_ns.response(
        int(HTTPStatus.BAD_REQUEST),
        'Validation error.'
    )
    @todo_ns.response(
        int(HTTPStatus.UNAUTHORIZED),
        'You do not have permission to delete a task.'
    )
    @todo_ns.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    def delete(self, id):
        '''Delete todo task.'''
        return delete_todo_task(id)
