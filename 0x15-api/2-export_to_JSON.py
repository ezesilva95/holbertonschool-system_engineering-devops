#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo = todo.json()

    t_list = []
    t_user = {}

    for task in todo:
        if task.get('userId') == int(user_id):
            t_dict = {"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.json().get('username')}
            t_list.append(t_dict)
        t_user[user_id] = t_list

    filename = user_id + '.json'
    with open(filename, mode='w') as jasonfile:
        json.dump(t_user, jasonfile)
