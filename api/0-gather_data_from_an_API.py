import requests
import sys


def get_employee_todo_progress(employee_id):
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

    else:
        print(f"Error: Unable to fetch TODO list for employee {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)
