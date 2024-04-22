#!/usr/bin/python3
"""
Export data in the JSON format using  task #0
"""
import json
import requests
import sys

if __name__ == "__main__":
    # API endpoint for fetching user data
    url = 'https://jsonplaceholder.typicode.com/users'

    # Fetch user data
    response = requests.get(url)
    users = response.json()

    # Create a dictionary to store tasks for all employees
    all_tasks = {}

    # Iterate over each user
    for user in users:
        user_id = user['id']
        username = user['username']

        # API endpoint for fetching tasks of a specific user
        tasks_url = f
        'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

        # Fetch tasks for the current user
        response = requests.get(tasks_url)
        tasks = response.json()

        # Store tasks in the dictionary
        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        # Add tasks to the dictionary with user_id as the key
        all_tasks[user_id] = user_tasks

    # Write tasks to a JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(all_tasks, f)

    print(f'Tasks for all employees have been written to {filename}')
