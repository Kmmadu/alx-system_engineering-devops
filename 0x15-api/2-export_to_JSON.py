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
    employeeId = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        employeeId)
    userUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employeeId)
    res = requests.get(userUrl)
    if res.status_code == 200:
        users = res.json()
        userName = users['username']

    res = requests.get(url)
    if res.status_code == 200:
        todo = res.json()
        user_json = []
        populate_user = {}
        for task in todo:
            user_json.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": userName
            })
        populate_user[employeeId] = user_json
        filename = '{}.json'.format(employeeId)

        with open(filename, 'w') as file:
            json.dump(populate_user, file)
