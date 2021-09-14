#!/usr/bin/python3
"""Export data in the JSON format.
"""

import csv
import json
import requests

if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    resp_user = requests.get(url_user)
    json_r_user = resp_user.json()

    big_dic = {}

    for user in json_r_user:
        user_id = user["id"]

        resp_todos = requests.get(url_todo.format(user_id))
        json_r_todos = resp_todos.json()

        user_name = user.get("username")

        val_l = []
        for task in json_r_todos:
            del task["userId"]
            del task["id"]
            task["task"] = task.pop("title")
            task["username"] = user_name
            val_l.append(task)

        big_dic[str(user_id)] = val_l

    json_fname = "todo_all_employees.json"

    with open(json_fname, 'w+') as fd_json:
        json.dump(big_dic, fd_json)
