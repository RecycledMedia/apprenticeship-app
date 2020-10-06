import os
import sqlite3


class TaskDatabase:
    def __init__(self, db_filename):
        self.filename = db_filename
        self.connection = None

    def get_connection(self):
        """ Return a connection to the database, creating one if it doesn't exist """
        if self.connection is None:
            self.connection = sqlite3.connect(self.filename, check_same_thread=False)

        return self.connection

    def close_connection(self):
        """ Close the connection to the database """
        if self.connection:
            self.connection.close()
        self.connection = None

    def get_cursor(self):
        """ Return a database cursor"""
        return self.get_connection().cursor()

    def execute(self, cursor, sql, parameters=None):
        """ Execute a SQL statement

        If the cursor is None, one will be automatically created
        """
        if cursor is None:
            cursor = self.connection.cursor()

        print(f"Executing SQL: {sql}")
        if parameters:
            print(f"Parameters: {parameters}")
            return cursor.execute(sql, parameters)

        cursor.execute(sql)
        self.get_connection().commit()

    def create_database(self):
        """ Create the tasks database """
        cursor = self.get_cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS tasks (
              id integer PRIMARY KEY,
              created_date text NOT NULL,
              content text NOT NULL,
              done boolean DEFAULT false,
              completed_date text
            );"""
        self.execute(cursor, sql)

    def delete_database(self):
        """ Delete the tasks database file """
        self.close_connection()

        os.unlink(self.filename)
        self.connection = None

    def add_task(self, content):
        """ Add a task """
        # WARNING: This is bad and can lead to SQL Injection attacks!
        sql = f"""
          INSERT INTO tasks (created_date, content) 
          VALUES (datetime('now'), '{content.replace("'", "''")}');
        """

        cursor = self.get_cursor()
        self.execute(cursor, sql)
        return cursor.lastrowid

    def rename_task(self, task_id, content):
        """ Rename a task """
        sql = "UPDATE tasks SET content = ? WHERE id = ?;"

        return self.execute(None, sql, (content, task_id))

    def set_task_done(self, task_id, done=True):
        if done:
            sql = "UPDATE tasks SET done = TRUE, completed_date = datetime('now') WHERE id = ?;"
        else:
            sql = "UPDATE tasks SET done = FALSE, completed_date = NULL WHERE id = ?;"

        return self.execute(None, sql, (task_id, ))

    def delete_task(self, task_id):
        """ Delete a task """
        sql = "DELETE FROM tasks WHERE id = ?;"

        return self.execute(None, sql, (task_id, ))

    def get_task(self, task_id):
        """ Retrieve a single task by id from the database """
        columns = ('id', 'created_date', 'content', 'done', 'completed_date')
        sql = f"SELECT {', '.join(columns)} FROM tasks WHERE id = ?;"

        cursor = self.get_cursor()
        self.execute(cursor, sql, (task_id, ))
        return self.make_result(columns, cursor.fetchall())[0]

    def get_tasks(self):
        """ Retrieve all tasks from the database """
        columns = ('id', 'created_date', 'content', 'done', 'completed_date')
        sql = f"SELECT {', '.join(columns)} FROM tasks ORDER BY id;"

        cursor = self.get_cursor()
        self.execute(cursor, sql)
        return self.make_result(columns, cursor.fetchall())

    def make_result(self, columns, rows):
        """ Helper function to convert lists of (list) results into a list of dicts """
        records = []
        for row in rows:
            records.append(dict(zip(columns, row)))

        return records
