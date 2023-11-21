#!/usr/bin/python3
"""Use this REST API, for a given employee ID, returns 
information about his/her TODO
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ script must display to stdout the employee todo list progress """
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = f"{base_url}/{employee_id}/todos"

    try:
        """ Fetching employee data"""
        employee_response = requests.get(f"{base_url}/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data["name"]

        """Fetching TODO list for the employee"""
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        """ Calculating progress"""
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo["completed"])
        percentage_complete = round((completed_tasks / total_tasks) * 100, 2)

        """ Displaying progress in a more user-friendly format"""
        print(
            f"Employee {employee_name} is done with tasks \
                ({completed_tasks}/{total_tasks}) ({percentage_complete}%):")

        for todo in todos:
            if todo["completed"]:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
