#!/usr/bin/python3
"""Exporting employee todo data in CSV format"""
import csv
import requests
from sys import argv


def fetch_and_export_data():
    """ Get the data from the API as requested """
    if len(argv) != 2:
        print("Usage: python script_name.py user_id")
        return

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    try:
        user_response = requests.get(f"{base_url}users/{user_id}")
        user_response.raise_for_status()
        user_data = user_response.json()

        todo_response = requests.get(
            f"{base_url}todos", params={'userId': user_id})
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        with open(f'{user_id}.csv', 'w', encoding='UTF-8') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            for task in todo_data:
                username = user_data.get('username')
                task_completed = task.get('completed')
                task_title = task.get('title')

                task_record = [user_id, username, task_completed, task_title]
                csv_writer.writerow(task_record)

        print("CSV file created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data from the API. Reason: {e}")


if __name__ == '__main__':
    fetch_and_export_data()
