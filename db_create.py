import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute sql commands
    c = connection.cursor()

    #create table
    c.execute("""
    CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
    status INTEGER NOT NULL)
    """)

    c.execute(
        'INSERT INTO tasks(name,due_date,priority,status)'
        'VALUES("Finish this tutorial","03/25/2015",10,1)'
    )

    c.execute(
        'INSERT INTO tasks(name,due_date,priority,status)'
        'VALUES("Finish Real Python Course 2","03/25/2015",10,1)'
    )
