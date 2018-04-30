#!/usr/bin/python3
"""
    Script uses REST API to return information about TODO list progress
    based on given employee ID
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    name = response.get("name")

    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    completed = 0
    tasks = []
    total = 0
    for line in requests.get(todo_url).json():
        if line.get('userId') == employee_id:
            total += 1
            if line.get('completed'):
                completed += 1
                tasks.append(line.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed,
                                                          total))
    for task in tasks:
        print("    {}".format(task))
