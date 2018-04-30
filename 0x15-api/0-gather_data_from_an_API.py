#!/usr/bin/python3
"""
    Script uses REST API to return information about TODO list progress
    based on given employee ID

    Output:
        Employee NAME is done with tasks(NUMBER_DONE/TOTAL_NUMBER_OF_TASKS):
            TASK_TITLE
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    name = response.get("name")

    done = 0
    tasks = []
    total = 0
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    for line in requests.get(todo_url).json():
        if line.get('userId') == employee_id:
            total += 1
            if line.get('completed'):
                done += 1
                tasks.append(line.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in tasks:
        print("    {}".format(task))
