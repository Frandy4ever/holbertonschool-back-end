#!/usr/bin/python3
""" Export data in the CSV format """
from sys import argv
import csv
import requests


def get_api():
    """ Retrieve data from the API """
    if len(argv) != 2:
        print("Usage: python script_name.py user_id")
        return

    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]

    try:
        user_response = requests.get(url + f'users/{uid}')
        user_response.raise_for_status()
        user = user_response.json()

        todo_response = requests.get(url + 'todos', params={'userId': uid})
        todo_response.raise_for_status()
        todo = todo_response.json()

        with open(f'{uid}.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            for employee in todo:
                user_id = uid
                username = user.get('username')
                task_comp = employee.get('completed')
                task_title = employee.get('title')

                emp_record = [user_id, username, task_comp, task_title]
                writer.writerow(emp_record)

        print("Number of tasks in CSV: OK")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    get_api()
