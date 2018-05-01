#!/usr/bin/python3
"""
    Export TODO list data to JSON
"""
import csv
import json
import requests
from sys import argv


def get_completed(employee_id):
    """
        Script uses REST API to return information about TODO list progress
        based on given employee ID

        Output:
            Employee NAME is done with tasks(NUMBER_DONE/TOTAL_NUMBER):
                TASK_TITLE
                TASK_TITLE
                ...
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


def save_to_CSV(employee_id):
    """
        Export TODO list data to CSV for given employee_id

        File name: USER_ID.csv

        Format of file:
            "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    filename = "{}.csv".format(employee_id)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    name = response.get("name")

    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_response = requests.get(todo_url).json()
    attrs = ["userId", "username", "completed", "title"]
    with open(filename, 'w') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=attrs)
        writer.writeheader()
        for line in todo_response:
            if line.get('userId') == employee_id:
                line['username'] = name
                del line['id']
                writer.writerow(line)


def get_todo_dict(employee_id):
    """
        Return dictionary of TODO list data for given employee id

        Format of dictionary:
            { "USER_ID":
            [  {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}},
               {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}}, ...
            ]
            }
    """
    filename = "{}.json".format(employee_id)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    name = response.get("name")

    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_response = requests.get(todo_url).json()
    attrs = ["userId", "username", "completed", "title"]
    todo_list = []
    for line in todo_response:
        if line.get('userId') == employee_id:
            line['username'] = name
            del line['id']
            todo_list.append(line)
    return {employee_id: todo_list}


def save_to_JSON(employee_id):
    """
        Export TODO list data to JSON for given employee_id

        File name: USER_ID.json

        Format of file:
            { "USER_ID":
            [  {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}},
               {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"}}, ...
            ]
            }
    """
    todo_list = json.dumps(get_todo_dict(employee_id))
    with open(filename, 'w') as f:
        f.write(todo_list)


if __name__ == "__main__":
    save_to_JSON(int(argv[1]))
