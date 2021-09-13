#!/usr/bin/python3
"""
This script returns information about an user TODO list progress. 
It receives the user id
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    user_request = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(user_id))
    user = json.loads(user_request.text)[0]
    todos_request = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    todo_list = json.loads(todos_request.text)
    done_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            done_tasks.append(task)

    with open('{}.csv'.format(user_id), mode='w') as file:
        for task in todo_list:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow([user_id,
                            user.get('username'),
                            task.get('completed'),
                            task.get('title')])
