#!/usr/bin/python3
"""Script exports data in the csv format"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Employee id argument required")
        sys.exit(1)

    emp_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        employee_json_data = user_response.json()
        username = employee_json_data.get("username")

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_json_data = todos_response.json()

        file_name = f"{emp_id}.csv"
        with open(file_name, mode='w', newline='') as csv_file:
            # writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            # writer.writerows(csv_data)
            # print(f"Data exported to {file_name}")
            for task in todos_json_data:
                csv_file.write('"{}", "{}", "{}", "{}"\n'.format(
                    emp_id, username, task['completed'], task['title']))

    except requests.exceptions.RequestException as e:
        print("Error fetchinf data")
        sys.exit(1)
