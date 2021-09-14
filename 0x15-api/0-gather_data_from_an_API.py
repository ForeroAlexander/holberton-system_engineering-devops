#!/usr/bin/python3
"""Is a Python script that, using this REST API, for a given=employee
ID, returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    request = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1])).json()

    EMPLOYEE_NAME = request.get("name")

    request = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()

    for i in request:
        if i.get("completed") is True:
            TASK_TITLE.append(i.get("title"))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(request)

    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))
