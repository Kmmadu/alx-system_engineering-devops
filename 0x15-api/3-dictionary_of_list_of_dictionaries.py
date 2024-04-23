#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    This export to the data to csv
    """
    url = 'https://jsonplaceholder.typicode.com/todos/'
    userUrl = 'https://jsonplaceholder.typicode.com/users/'

    populate_user = {}
    res = requests.get(userUrl)
    if res.status_code == 200:
        users = res.json()

    res = requests.get(url)
    if res.status_code == 200:
        todos = res.json()

    for user in users:
        user_json = []
        for todo in todos:
            if user.get('id') == todo.get('userId'):
                user_json.append({
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })
            populate_user[user.get('id')] = user_json

    with open('todo_all_employees.json', 'w') as file:
        json.dump(populate_user, file)
