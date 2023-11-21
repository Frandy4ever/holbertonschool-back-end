#!/usr/bin/python3

import requests
import sys


def display_employee_progress(employee_id):
    """ script must display to stdout the employee todo list progress """
    url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{url}/todos"
    employee_url = f"{url}/users/{employee_id}"

    try:
        employee_data = requests.get(employee_url).json()
        todo_data = requests.get(
            todo_url, params={"userId": employee_id}).json()

        employee_name = employee_data.get("name")
        completed_tasks = [i["title"] for i in todo_data if i["completed"]]
        completed = len(completed_tasks)
        total_complete = len(todo_data)

        print(f"Employee {employee_name} is done with tasks({completed}/{total_complete})")
        for task in completed_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    display_employee_progress(int(sys.argv[1]))
