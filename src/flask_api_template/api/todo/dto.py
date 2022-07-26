from flask_restx import Model
from flask_restx import fields, inputs
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
    type=inputs.date(),
    location='form',
    required=True,
    nullable=False,
)
todo_reqparser.add_argument(
    name='finished',
    type=bool,
    location='form',
    required=True,
    nullable=False
)

todo_model = Model(
    'TodoTask',
    {
        'assigned': fields.String,
        'task': fields.String,
        'deadline': fields.String,
        'finished': fields.Boolean,
    }
)