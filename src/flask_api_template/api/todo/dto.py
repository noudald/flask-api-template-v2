from flask_restx import Model
from flask_restx import inputs, fields
from flask_restx.reqparse import RequestParser


todo_reqparser = RequestParser(bundle_errors=True)
todo_reqparser.add_argument(
    name='assigned',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_reqparser.add_argument(
    name='task',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_reqparser.add_argument(
    name='deadline',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_reqparser.add_argument(
    name='finished',
    type=inputs.boolean,
    location='form',
    required=True,
    nullable=False
)

todo_model = Model(
    'TodoTask',
    {
        'id': fields.Integer,
        'assigned': fields.String,
        'task': fields.String,
        'deadline': fields.String,
        'finished': fields.Boolean,
    }
)

todo_list_model = Model(
    'TodoList',
    {
        'status': fields.String,
        'message': fields.String,
        'tasks': fields.List(fields.Nested(todo_model)),
    }
)
