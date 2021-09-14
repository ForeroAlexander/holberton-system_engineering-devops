#!/usr/bin/python3
"""Export data in the JSON format.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    USER_ID = argv[1]

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'
    resp_todos = requests.get(url_todo.format(USER_ID))
    resp_user = requests.get(url_user.format(USER_ID))
    json_r_todos = resp_todos.json()
    json_r_user = resp_user.json()

    USERNAME = json_r_user.get("username")

    json_fname = USER_ID + ".json"

    val_l = []
    for task in json_r_todos:
        del task["userId"]
        del task["id"]
        task["task"] = task.pop("title")
        task["username"] = USERNAME
        val_l.append(task)
    dic = {str(USER_ID): val_l}

    with open(json_fname, 'w+') as fd_json:
        json.dump(dic, fd_json)
