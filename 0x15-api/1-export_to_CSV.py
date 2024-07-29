#!/usr/bin/python3
"""
A script to export employee's to-do list to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com'

    # Get employee details
    employee_url = f'{base_url}/users/{employee_id}'
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_data = employee_response.json()
    username = employee_data.get('username')

    # Get tasks
    tasks_url = f'{base_url}/todos?userId={employee_id}'
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            csv_writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
