from apiflask.schemas import Schema
from apiflask import fields

"""
class task:
  id integer
  content string
  is_complete Boolean
  date_added Datetime

"""


class TaskOutPutSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_completed = fields.Boolean()


class TaskCreateSchema(Schema):
    content = fields.String(required=True)


class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_completed = fields.Boolean(required=True)
