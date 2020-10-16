import os

from flask import Flask, make_response, request
from flask import render_template
from flask import redirect

from db import TaskDatabase

app = Flask(__name__)

DATA_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(DATA_DIR, 'tasks.sqlite')


db = TaskDatabase(DB_FILE)
db.create_database()


@app.route('/')
def tasks_list():
    tasks = db.get_tasks()
    return render_template('list.html', tasks=tasks, hide_done=False)


@app.route('/hide_done')
def undone_tasks_list():
    tasks = db.get_undone_tasks()
    return render_template('list.html', tasks=tasks, hide_done=True)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'

    db.add_task(content)
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = db.get_task(task_id)
    if not task:
        return redirect('/')

    db.delete_task(task_id)
    return redirect('/')


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    db.set_task_done(task_id)
    return redirect('/')


if __name__ == '__main__':
    app.run()
