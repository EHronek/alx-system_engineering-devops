#!/usr/bin/python3
""" Exports employee todo """
import json
import sys
import requests

if __name__ == "__main__":
    emp_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    emp_data = user_response.json()
    username = emp_data.get("username")

    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_json_data = todos_response.json()

    tasks = {str(emp_id): []}
    for task in todos_json_data:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        tasks[emp_id].append({
                              "task": TASK_TITLE,
                              "completed": TASK_COMPLETED_STATUS,
                               "username": username})


    file_name = f"{emp_id}.json"
    with open(file_name, 'w') as json_file:
         json.dump(tasks, json_file, indent=4)
