#!/usr/bin/python3
"""
Script to export user-specific data from the JSONPlaceholder API in JSON format.

Functions:
    export_data_to_json(user_id):
        Exports user-related data, including completed tasks, to a JSON file.
        Args:
            user_id (int): The ID of the user for whom data is exported.

Usage:
    python script_name.py user_id
"""
import json
import requests
from sys import argv

BASE_API_URL = 'https://jsonplaceholder.typicode.com'


def export_data_to_json(user_id):
    """
    Export user-related data to a JSON file.

    Args:
        user_id (int): The ID of the user for whom data is exported.

    Raises:
        requests.exceptions.RequestException: If there is an issue with API requests.
    """
    try:
        user_response = requests.get(f"{BASE_API_URL}/users/{user_id}")
        user_response.raise_for_status()
        user_data = user_response.json()

        todo_response = requests.get(f"{BASE_API_URL}/todos?userId={user_id}")
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        exported_data = {
            user_id: [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user_data['username']
                }
                for task in todo_data
            ]
        }

        with open(f"{user_id}_exported_data.json", mode='w') as json_file:
            json.dump(exported_data, json_file)

        print(f"Data has been exported to {user_id}_exported_data.json")

    except requests.exceptions.RequestException as error:
        print(f"Error: Unable to fetch data from the API. {error}")


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script_name.py user_id")
        exit(1)

    try:
        user_id = int(argv[1])
        export_data_to_json(user_id)
    except ValueError:
        print("Error: User ID must be an integer.")
        exit(1)
