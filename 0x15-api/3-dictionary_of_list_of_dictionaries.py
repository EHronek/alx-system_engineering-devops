#!/usr/bin/python3
""" Export data in json format"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"


    users_response = requests.get(users_url)
    users_response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    users_data = users_response.json()

    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = str(user["id"])  # Convert user ID to string
        username = user["username"]
        user_tasks = []

        for task in todos_data:
            if task["userId"] == user["id"]:
                user_tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        all_tasks[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)

    print(f"Data exported to {filename}")
