#!/usr/bin/python3
"""Exports data in the CSV format.
"""

import csv
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

    user_name = json_r_user.get("username")

    csv_fname = user_id + ".csv"

    with open(csv_fname, 'w+') as fd_csv:

        # Object used to write in CSV format
        csv_writer = csv.writer(fd_csv, quoting=csv.QUOTE_ALL)

        for task in json_r_todos:
            csv_writer.writerow([user_id,
                                 user_name,
                                 task['completed'], task['title']])
