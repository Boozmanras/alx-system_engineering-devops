#!/usr/bin/python3
"""
This module exports the tasks of a specific employee to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Fetch employee ID from command line argument
    employee_id = sys.argv[1]
    
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_data = requests.get(user_url).json()
    username = user_data.get('username')
    
    # Fetch todos data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_data = requests.get(todos_url).json()
    
    # Prepare data for JSON export
    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": username
    } for todo in todos_data]
    
    data = {employee_id: tasks}
    
    # Export data to JSON file
    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)
