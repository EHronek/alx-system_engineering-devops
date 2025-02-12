#!/usr/bin/python3
"""Script tghat returns information about an employee using given REST API"""

import requests
import sys


if __name__ == "__main__":    
    """Define the base url for the api"""
    emp_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        employee_data = user_response.json()
        emp_name = employee_data.get("name")

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)
        completed_tasks_number = len(completed_tasks)

        print(f"Employee {emp_name} is done with tasks({completed_tasks_number}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
