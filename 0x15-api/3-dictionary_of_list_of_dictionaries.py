#!/usr/bin/python3
"""
This script returns information about an user TODO list progress.
It receives the user id
"""

import json
import requests

if __name__ == "__main__":

    user_request = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    users = json.loads(user_request.text)
    todos_request = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    tasks = json.loads(todos_request.text)

    users_dict = {}
    task_index = 0
    for user in users:
        users_dict[user.get('id')] = []
        while(task_index < len(tasks) and
                tasks[task_index].get('userId') == user.get('id')):
            task_dict = {}
            task_dict['username'] = user.get('username')
            task_dict['task'] = tasks[task_index].get('title')
            task_dict['completed'] = tasks[task_index].get('completed')
            users_dict[user.get('id')].append(task_dict)
            task_index += 1

    with open('todo_all_employees.json', "w") as file:
        json.dump(users_dict, file)
