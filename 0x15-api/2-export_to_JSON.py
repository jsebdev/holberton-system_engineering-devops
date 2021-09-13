#!/usr/bin/python3
"""
This script returns information about an user TODO list progress. 
It receives the user id
"""

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

    user_dict = {}
    user_dict[user_id] = []
    for task in todo_list:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = user.get('username')
        user_dict[user_id].append(task_dict)

    with open('{}.json'.format(user_id), "w") as file:
        json.dump(user_dict, file)

