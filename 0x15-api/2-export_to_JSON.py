#!/usr/bin/python3
""" Exports employee todo """
import json
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    emp_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        emp_data = user_response.json()
        username = emp_data.get("username")

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_json_data = todos_response.json()

        tasks = []
        for task in todos_json_data:
            tasks.append({
                "task": task["title"],  # TASK_TITLE
                "completed": task["completed"],  # TASK_COMPLETED_STATUS
                "username": username  # USERNAME
            })

        json_data = {str(emp_id): tasks}

        file_name = f"{emp_id}.json"
        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    except requests.exceptions.RequestException as e:
        sys.exit(1)
