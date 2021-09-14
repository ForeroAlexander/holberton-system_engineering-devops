#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'
    resp_todos = requests.get(url_todo.format(user_id))
    resp_user = requests.get(url_user.format(user_id))
    json_r_todos = resp_todos.json()
    json_r_user = resp_user.json()

    EMPLOYEE_NAME = json_r_user.get("name")

    for i in resp_todos:
        if i.get("completed") is True:
                TOTAL_NUMBER_OF_TASKS = len(json_r_todos)
    TASK_TITLE.append(i.get("title"))
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))

    for dic in TASK_TITLE:
        print("\t {}".format(dic.get("task")))
