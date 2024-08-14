#!/usr/bin/env python3

"""This python script uses REST API, for a given employee ID,
    returns information about his/her TODO list progress"""

import requests
import sys
if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users/"
    url = baseUrl + employeeId
    response = requests.get(url)
    employeeName = response.json().get('name')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    completed = 0
    tasks_completed = []
        
    for task in tasks:
        if task.get('completed'):
            tasks_completed.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
            .format(employeeName, completed, len(tasks)))

        
    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
