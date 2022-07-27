from http import HTTPStatus

from flask_restx import Namespace, Resource

from flask_api_template.api.todo.dto import (
    todo_add_reqparser,
    todo_get_reqparser,
    todo_update_reqparser,
    todo_model
)
from flask_api_template.api.todo.business import (
    new_todo_task,
    update_todo_task,
    get_todo_task,
    delete_todo_task,
)


todo_ns = Namespace(name='todo', validate=True)
todo_ns.models[todo_model.name] = todo_model


@todo_ns.route('/task', endpoint='task')
class TodoTask(Resource):
    @todo_ns.expect(todo_add_reqparser)
    @todo_ns.response(
        int(HTTPStatus.CREATED),
        'New task was successfully create.'
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
    def post(self):
        # New todo task
        pass

    @todo_ns.expect(todo_get_reqparser)
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
        # Get todo task
        pass

    @todo_ns.expect(todo_update_reqparser)
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
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    @todo_ns.marshal_with(todo_model)
    def update(self, id):
        # Update todo task
        pass

    @todo_ns.expect(todo_get_reqparser)
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
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    def delete(self, id):
        # Delete todo task
        pass