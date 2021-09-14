#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'
    resp_todos = requests.get(url_todo.format(user_id))
    resp_user = requests.get(url_user.format(user_id))
    json_r_todos = resp_todos.json()
    json_r_user = resp_user.json()

    user_name = json_r_user.get("name")

    total_tasks = len(json_r_todos)
    filteredData = list(filter(lambda d: d['completed'] is True, json_r_todos))
    completed_tasks = len(filteredData)

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          completed_tasks,
                                                          total_tasks))

    for dic in filteredData:
        print("\t {}".format(dic.get("title")))
