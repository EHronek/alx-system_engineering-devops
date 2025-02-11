#!/usr/bin/python3
"""Script exports data in the csv format"""
import csv
import requests
import sys


def export_employee_data_to_csv(emp_id):
    """exports employee data to csv file"""
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

        csv_data = []
        for task in todos_json_data:
            csv_data.append([
                emp_id,
                username,
                str(task['completed']),
                task['title']
            ])

        file_name = f"{emp_id}.csv"
        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            writer.writerows(csv_data)
            print(f"Data exported to {file_name}")

    except requests.exceptions.RequestException as e:
        print("Error fetchinf data")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide an employee id as argument")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        export_employee_data_to_csv(emp_id)
    except ValueError:
        print("Employee id should be an integer!")
        sys.exit(1)
