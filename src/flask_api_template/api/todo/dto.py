from flask_restx import Model
from flask_restx import fields
from flask_restx.reqparse import RequestParser


todo_add_reqparser = RequestParser(bundle_errors=True)
todo_add_reqparser.add_argument(
    name='assigned',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_add_reqparser.add_argument(
    name='task',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_add_reqparser.add_argument(
    name='deadline',
    type=str,
    location='form',
    required=True,
    nullable=False,
)
todo_add_reqparser.add_argument(
    name='finished',
    type=bool,
    location='form',
    required=True,
    nullable=False
)

todo_get_reqparser = RequestParser(bundle_errors=True)
todo_get_reqparser.add_argument(
    name='id',
    type=int,
    location='form',
    required=True,
    nullable=False,
)

todo_update_reqparser = todo_add_reqparser.copy()
todo_update_reqparser.add_argument(
    name='id',
    type=int,
    location='form',
    required=True,
    nullable=False,
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
