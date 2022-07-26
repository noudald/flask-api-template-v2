from http import HTTPStatus

from flask_restx import Namespace, Resource

from flask_api_template.api.todo.dto import todo_reqparser, todo_model
from flask_api_template.api.todo.business import (
    new_todo_task,
    update_todo_task,
    get_todo_task,
    delete_todo_task,
)


todo_ns = Namespace(name='todo', validate=True)
todo_ns.models[todo_model.name] = todo_model


@todo_ns.route('/task/<int:id>', endpoint='task')
class TodoTask(Resource):
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
        int(HTTPStatus.INTERNAL_SERVER_ERROR),
        'Internal server error.'
    )
    @todo_ns.marshal_with(todo_model)
    def post(self, id):
        # New todo task
        pass

    def get(self, id):
        # Get todo task
        pass

    def update(self, id):
        # Update todo task
        pass

    def delete(self, id):
        # Delete todo task
        pass
