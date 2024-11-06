from datetime import datetime
import sqlite3
import sys
import os
from tabulate import tabulate

filename = "tasks.db"

def add_task():
    # Insert the task
    status='pending'
    task_info = input("enter task description:\n")
    task_datetime = datetime.now().strftime("%F %T")
    cursor.execute(
        """
    INSERT INTO tasks (status, task_info, task_datetime)
    VALUES (?, ?, ?)
    """,
        (status, task_info, task_datetime),
    )
    connection.commit()
    print("Task succesfully added!\n")

def view_tasks():
    print("Current Tasks:\n")
    existing_tasks = cursor.execute("SELECT * FROM tasks")
    print(tabulate(existing_tasks,headers=['id','status','task','date']))
    # for task in existing_tasks:
    #     task_info = f"{task[1]}> {task[0]}. \t{task[2]} \t{task[3]}"
    #     print(task_info)
    print()

def update_task():
    view_tasks()
    task_id = input("Enter id of the task to select:")
    res = cursor.execute(f"""
    SELECT EXISTS(SELECT 1 FROM tasks WHERE id={task_id})
    """)
    if(res.fetchone()[0]):
        # print("row selected!")
        print("enter task to perfom:")
        print("1. mark as completed\n")
        choice = input("To-Do>update-choice>")
        new_status = "completed"
        if(choice=="1"):
            cursor.execute('''
                UPDATE tasks SET status = ? WHERE id = ?
            ''', (new_status, task_id))
            connection.commit()
            print(f"Task {task_id} is now marked as completed.")
    else:
        print("error: row does not exist")
def delete_task():
    view_tasks()
    task_id = input("Enter id of the task to delete:")
    # check row exists or not
    res = cursor.execute(f"""
    SELECT EXISTS(SELECT 1 FROM tasks WHERE id={task_id})
    """)
    if(res.fetchone()[0]):
        cursor.execute('''
            DELETE FROM tasks WHERE id = ?
        ''', (task_id,))
        connection.commit()
        print(f"Task {task_id} is now deleted.")
    else:
        print("error: row does not exist")

def help():
    print("List of supported commands:")
    print("add - Add a new task")
    print("view/track - View/Track all tasks")
    print("update/mark - Update a task")
    print("delete - Delete a task")
    print()

def askChoice():
    print("To-Do Manager v1")
    print("- press help for commands")
    print("- press exit/^C to Exit")
    print()
    while True:
        choice = input("To-Do>")
        if choice == "help":
            help()
        elif choice == "add":
            add_task()
        elif choice == "view" or choice == "track":
            view_tasks()
        elif choice == "update" or choice == "mark":
            update_task()
        elif choice == "delete" or choice=="del":
            delete_task()
        elif choice == "exit":
            print("Exiting the To-Do Manager.")
            break

if __name__ == "__main__":
    # create db if not created
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    # create table if not created
    cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL,
                task_info TEXT NOT NULL,
                task_datetime TEXT NOT NULL -- Use ISO 8601 format
            )
            """
    )
    connection.commit()
    
    try:
        askChoice()
    except KeyboardInterrupt:
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    