from flask_api_template import db

from flask_api_template.util.datetime_util import (
    utc_now,
)

class TodoTask(db.Model):
    __tablename__ = 'todo_task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assigned = db.Column(db.String(255))
    task = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.DateTime, default=utc_now())
    finished = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return ('<TodoTask'
                f' id={self.id}'
                f', assigned={self.assigned}'
                f', task=\"{self.task}\"'
                f', deadline={self.deadline}'
                f', finished={self.finished}'
                '>')

    @classmethod
    def find_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()

    @classmethod
    def list_all_tasks(cls):
        return cls.query.all()
