#!/usr/bin/python3
"""Export data in Comma Separated Values format"""
import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    """Retrieve data via API"""
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    response = requests.get(url)
    todos = response.json()

    user_id = todos[0]['userId']
    username = todos[0]['username']

    total_tasks = len(todos)

    """Create CSV file with employee data"""
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        """Write TODO list data to CSV"""
        for todo in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(todo['completed']),
                "TASK_TITLE": todo['title']
            })

    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        """Parse employee ID from command-line argument"""
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
