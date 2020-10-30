import os

from flask import Flask, request
from flask import render_template
from flask import redirect

from db import TaskDatabase

app = Flask(__name__)

DATA_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(DATA_DIR, 'tasks.sqlite')


db = TaskDatabase(DB_FILE)
db.create_database()


def redirect_to_form():
    ref = request.headers.get('Referer')
    if not ref:
        ref = '/'
    return redirect(ref)

@app.route('/')
def tasks_list():
    hide_done = int(request.cookies.get('hide_done', 0))

    if hide_done:
        tasks = db.get_undone_tasks()
    else:
        tasks = db.get_tasks()
    return render_template('list.html', tasks=tasks, hide_done=hide_done)

@app.route('/1')
def tasks_list_1():
    hide_done = int(request.cookies.get('hide_done', 0))

    if hide_done:
        tasks = db.get_undone_tasks()
    else:
        tasks = db.get_tasks()
    return render_template('list_1.html', tasks=tasks, hide_done=hide_done)

@app.route('/2')
def tasks_list_2():
    hide_done = int(request.cookies.get('hide_done', 0))

    if hide_done:
        tasks = db.get_undone_tasks()
    else:
        tasks = db.get_tasks()
    return render_template('list_2.html', tasks=tasks, hide_done=hide_done)

@app.route('/3')
def tasks_list_3():
    hide_done = int(request.cookies.get('hide_done', 0))

    if hide_done:
        tasks = db.get_undone_tasks()
    else:
        tasks = db.get_tasks()
    return render_template('list_3.html', tasks=tasks, hide_done=hide_done)

@app.route('/4')
def tasks_list_4():
    hide_done = int(request.cookies.get('hide_done', 0))

    if hide_done:
        tasks = db.get_undone_tasks()
    else:
        tasks = db.get_tasks()
    return render_template('list_4.html', tasks=tasks, hide_done=hide_done)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'

    db.add_task(content)
    return redirect_to_form()

@app.route('/hide_done/<int:hide_done>')
def filter_tasks(hide_done):
    resp = redirect_to_form()
    resp.set_cookie('hide_done', str(hide_done))
    return resp

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = db.get_task(task_id)
    if not task:
        return redirect('/')

    db.delete_task(task_id)
    return redirect_to_form()


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    db.set_task_done(task_id)
    return redirect_to_form()


if __name__ == '__main__':
    app.run()
