#!/usr/bin/python3
"""With API use employee ID to retrieve info about their todo list."""
import requests


def show_employee_todo_progress(employee_id):
    """ Display the employee's todo list progress """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos"

    try:
        """Fetch employee data"""
        employee_data = requests.get(employee_url)
        employee_data.raise_for_status()
        employee_data = employee_data.json()

        """Fetch todo data"""
        todo_data = requests.get(todo_url, params={"userId": employee_id})
        todo_data.raise_for_status()
        todo_data = todo_data.json()

        employee_name = employee_data.get("name")
        completed_tasks = [task["title"]
                           for task in todo_data if task["completed"]]
        num_done = len(completed_tasks)
        num_total = len(todo_data)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_done, num_total))
        for task_title in completed_tasks:
            print(f"\t {task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        show_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
