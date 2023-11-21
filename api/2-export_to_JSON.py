#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys


def export_to_json(user_id):
    """ Gathers todo list data for specified user & exports to JSON file """
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

        employee_name = next(
            person['username'] for person in users if person['id'] == user_id
        )

        found = next(
            todo['userId'] for todo in todos if todo['userId'] == user_id
        )
    except requests.exceptions.RequestException as req_error:
        print('ERROR:', req_error)
        sys.exit('Please try again.')

    except StopIteration:
        sys.exit("ID not found.")

    employee_task_data = {
        found: list(
            {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': employee_name
            }
            for todo in todos if todo['userId'] == user_id
        )
    }

    with open(f'{user_id}.json', 'w', encoding='UTF-8') as json_file:
        json.dump(employee_task_data, json_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Please enter only the requested employee's ID number")
    elif not sys.argv[1].isdigit():
        sys.exit("Please input employee's ID number (whole digit)")
    else:
        user_id = int(sys.argv[1])
    export_to_json(user_id)
