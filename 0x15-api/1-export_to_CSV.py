#!/usr/bin/python3
"""Exports data in the CSV format.
"""

import csv
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

    csv_fname = USER_ID + ".csv"

    with open(csv_fname, 'w+') as fd_csv:

        # Object used to write in CSV format
        csv_writer = csv.writer(fd_csv, quoting=csv.QUOTE_ALL)

        for todo in json_r_todos:
            TASK_COMPLETED_STATUS = todo.get("completed")
            TASK_TITLE = todo.get('title')
            csv_writer.writerow([USER_ID,
                                USERNAME,
                                TASK_COMPLETED_STATUS,
                                TASK_TITLE])
