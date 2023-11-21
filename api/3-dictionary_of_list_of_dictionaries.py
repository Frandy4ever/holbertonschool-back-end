#!/usr/bin/python3
"""Export data in JSON format"""
import json
import sys
import requests


def export_all_to_json():
    """ Gathers todo list data for all users & exports to JSON file """
    try:
        todos_response = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            timeout=30
        )
        todos_response.raise_for_status()
        todos = todos_response.json()

        users_response = requests.get(
            'https://jsonplaceholder.typicode.com/users',
            timeout=30
        )
        users_response.raise_for_status()
        users = users_response.json()

    except requests.exceptions.RequestException as req_error:
        print('ERROR:', req_error)
        sys.exit('Please try again.')

    employee_task_data = {
        user_id['userId']: list(
            {
                'username': next(
                    person['username']
                    for person in users if person['id'] == todo['userId']
                ),
                'task': todo['title'],
                'completed': todo['completed'],
            }
            for todo in todos if todo['userId'] == user_id['userId']
        )
        for user_id in todos
    }

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employee_task_data, json_file)


if __name__ == '__main__':
    export_all_to_json()
