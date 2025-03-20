#!/usr/bin/python3
"""
module contains a Python script that using REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users/{employee_id}").json()
    completed_params = {"userId": employee_id, "completed": "true"}
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()
    complete = requests.get(f"{url}todos", params=completed_params).json()
    name = users.get('name')
    print(f"Employee {name} is done with tasks({len(complete)}/{len(todos)}):")
    for value in complete:
        print(f"\t {value.get('title')}")
