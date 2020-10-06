from unittest import TestCase

from db import TaskDatabase


class DatabaseTestCase(TestCase):
    def setUp(self):
        self.db = TaskDatabase('test.sqlite')
        self.db.create_database(recreate=True)

    def tearDown(self):
        self.db.delete_database()

    def test_insert(self):
        task_1_id = self.db.add_task("This is a test item")
        task_2_id = self.db.add_task("This is another test item")

        tasks = self.db.get_tasks()

        self.assertEqual(len(tasks), 2)

        self.assertEqual(tasks[0]["id"], task_1_id)
        self.assertEqual(tasks[0]["content"], "This is a test item")
        self.assertEqual(tasks[0]["done"], False)
        self.assertEqual(tasks[1]["id"], task_2_id)
        self.assertEqual(tasks[1]["content"], "This is another test item")
        self.assertEqual(tasks[1]["done"], False)

    def test_task_done(self):
        task_id = self.db.add_task("This is a test item")

        self.db.set_task_done(task_id, True)

        task = self.db.get_task(task_id)
        self.assertEqual(task["done"], True)

        self.db.set_task_done(task_id, False)

        task = self.db.get_task(task_id)
        self.assertEqual(task["done"], False)

    def test_rename_task(self):
        task_id = self.db.add_task("This is a test item")

        self.db.rename_task(task_id, "This is the new name")

        tasks = self.db.get_tasks()

        self.assertEqual(len(tasks), 1)

        self.assertEqual(tasks[0]["content"], "This is the new name")

    def test_delete_task(self):
        task_id = self.db.add_task("This is a test item")
        self.db.delete_task(task_id)

        tasks = self.db.get_tasks()

        self.assertEqual(len(tasks), 0)
