#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))

    USERNAME = user.json().get('username')

    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    filename = user_id + '.csv'
    with open(filename, mode='w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in todo.json():
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, USERNAME, task.get('completed'),
                                task.get('title')])
