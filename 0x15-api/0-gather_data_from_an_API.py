#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))

    EMPLOYEE_NAME = user.json().get('name')

    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for task in todo.json():
        if task.get('userId') == int(user_id):
            TOTAL_NUMBER_OF_TASKS +=1
            if task.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))
    for tasks in TASK_TITLE:
        print("\t {}".format(tasks))
