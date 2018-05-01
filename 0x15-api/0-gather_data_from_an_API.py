#!/usr/bin/python3
"""
    Script uses REST API to return information about TODO list progress
    based on given employee ID
"""
import requests
from sys import argv


def get_completed(employee_id):
    """
        Script uses REST API to return information about TODO list progress
        based on given employee ID

        Output:
            Employee NAME is done with tasks(NUMBER_DONE/TOTAL_NUMBER):
                TASK_TITLE
    """
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
        print("\t {}".format(task))


if __name__ == "__main__":
    get_completed(int(argv[1]))
