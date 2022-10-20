from apiflask import APIFlask, abort
from flask import jsonify
from db import session, Task
from schemas import TaskOutPutSchema, TaskCreateSchema, TaskUpdateSchema

# initialize APIFLASK
app = APIFlask(__name__)


@app.get("/")
def index():
    return {"name": "Divine Ibeme"}


"""
    get  /task get_all_task
    post  / task create_task
    get  / <task id> get_task_by_id
    put  / <task id>update_task
    delete / <task id> delete_task

"""


@app.get("/tasks")
def get_all_task():
    post = session.query(Task).all()
    schema = TaskOutPutSchema()
    result = schema.dump(post)
    return jsonify(result)


@app.post("/tasks")
@app.input(TaskCreateSchema)
@app.output(TaskOutPutSchema)
def create_tasks(data):
    content = data.get("content")
    new_task = Task(content=content)

    session.add(new_task)
    session.commit()

    return new_task, 201


# getting the task_id
@app.get("/tasks/<int:task_id>/")
@app.output(TaskOutPutSchema)
def get_tasks_by_id(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task is not None:
        return task, 200

    abort(404)


# updating tasks
@app.put("/tasks/<int:task_id>/")
@app.input(TaskUpdateSchema)
@app.output(TaskOutPutSchema)
def update_task(task_id, data):
    content = data.get("content")
    is_completed = data.get("is_completed")

    task_to_update = session.query(Task).filter_by(id=task_id).first()
    task_to_update.is_completed = is_completed
    task_to_update.content = content

    session.commit()
    return task_to_update


# deleting from database
@app.delete("/tasks/<int:task_id>/")
def delete_task(task_id):
    task_to_delete = session.query(Task).filter_by(id=task_id).first()

    session.delete(task_to_delete)
    session.commit()
    return {"message": "deleted"}, 204
