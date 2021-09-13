#!/usr/bin/python3
"""
This script returns information about an user TODO list progress. 
It receives the user id
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    user_request = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(argv[1]))
    user = json.loads(user_request.text)[0]
    todos_request = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    todo_list = json.loads(todos_request.text)
    done_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            done_tasks.append(task)

    print('Employee {} is done with tasks({}/{})'.format(user.get('name'),
          len(done_tasks), len(todo_list)))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
