#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Endpoint URL for the API
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)

    # Fetching data from the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        exit(1)

    try:
        data = response.json()
        # Check if data is empty
        if not data:
            print("Error: No data found for the provided employee ID")
            exit(1)

        # Print API response for debugging
        print("API Response:", data)

        # Count completed tasks
        completed_tasks = [task for task in data if task.get('completed')]
        total_tasks = len(data)

        # Displaying employee TODO list progress
        print(
                "Employee {} is done with tasks({}/{}):".format(
                    data[0]['name'], len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t", task['title'])
    except ValueError:
        print("Error: Failed to parse JSON response from the API")
        exit(1)
