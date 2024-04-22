#!/usr/bin/python3
"""
This module exports task data for a given employee ID to a JSON file.
"""
import json
import requests
import sys


def export_tasks_to_json(user_id):
    """
    Fetches tasks for a given employee and exports them to a JSON file.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data")
        return

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")
    user_tasks = []

    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        user_tasks.append(task_dict)

    tasks_json = {str(user_id): user_tasks}

    with open(f"{user_id}.json", 'w') as jsonfile:
        json.dump(tasks_json, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_tasks_to_json(sys.argv[1])
