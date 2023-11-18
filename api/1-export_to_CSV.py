#!/usr/bin/python3

import requests
import sys
import csv

if __name__ == "__main__":
    def get_employee_todo_progress(employee_id):
        """
        Retrieves and displays the TODO list progress of a given employee using the JSONPlaceholder API.
        Also exports the data to a CSV file.

        Parameters:
            employee_id (int): The ID of the employee for whom the TODO list progress is to be retrieved.

        Raises:
            ValueError: If the employee ID is not a positive integer.

        Returns:
            None
        """
        api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

        response = requests.get(api_url)

        if response.status_code == 200:
            todos = response.json()

            employee_name = todos[0]['username']

            total_tasks = len(todos)
            completed_tasks = sum(1 for todo in todos if todo['completed'])

            print(
                f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

            for todo in todos:
                if todo['completed']:
                    print(f"\t{todo['title']}")

            # Export data to CSV file
            export_to_csv(employee_id, employee_name, todos)
        else:
            print(
                f"Error: Unable to fetch TODO list for employee {employee_id}")

    def export_to_csv(employee_id, employee_name, todos):
        """
        Exports the employee's TODO list data to a CSV file.

        Parameters:
            employee_id (int): The ID of the employee.
            employee_name (str): The name of the employee.
            todos (list): List of TODO items for the employee.

        Returns:
            None
        """
        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            for todo in todos:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": "Completed" if todo['completed'] else "Incomplete",
                    "TASK_TITLE": todo['title']
                })

            print(f"Data exported to {csv_filename}")

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)
