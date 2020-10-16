from app import db

for task_number in range(1, 100):
    task_id = db.add_task(f"Task number {task_number}")
    db.set_task_done(task_id)
    task = db.get_task(task_id)
    print(f"Created and marked task number {task_number} (id) {task_id} done! {task['done']}")

db.close_connection()
