#!/usr/bin/python3
"""
This module exports the tasks of all employees to a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(users_url).json()
    
    all_tasks = {}
    
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        
        # Fetch todos for the user
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos_data = requests.get(todos_url).json()
        
        # Prepare tasks list for the user
        tasks = [{
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in todos_data]
        
        all_tasks[user_id] = tasks
    
    # Export all tasks to JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as json_file:
        json.dump(all_tasks, json_file)
