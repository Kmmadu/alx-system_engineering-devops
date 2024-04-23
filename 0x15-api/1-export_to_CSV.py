#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import csv
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

        csv_name = "{}.csv".format(employeeId)
        with open(csv_name, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            # writer.writeheader()
            for task in todo:
                writer.writerow([
                    employeeId, userName,
                    task.get('completed'),
                    task.get('title')])
