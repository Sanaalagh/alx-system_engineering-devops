#!/usr/bin/python3
"""
Exports data from a REST API to CSV for a given employee ID.
"""

import csv
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
    data = response.json()

    # Writing data to CSV file
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
                ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in data:
            writer.writerow(
                    [employee_id, task['username'], str(
                        task['completed']), task['title']])
