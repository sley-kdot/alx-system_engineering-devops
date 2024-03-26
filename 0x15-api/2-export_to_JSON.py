#!/usr/bin/python3
"""
module contains a Python script to export data in the JSON format
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users/{employee_id}").json()
    completed_params = {"userId": employee_id, "completed": "true"}
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()
    complete = requests.get(f"{url}todos", params=completed_params).json()

    file_name = f"{employee_id}.json"

    new_list = []

    for val in todos:
        new_list.append({
                "task": val.get("title"),
                "completed": val.get("completed"),
                "username": users.get("username")})

    data = {employee_id: new_list}

    with open(file_name, "w", newline='') as json_file:
        json.dump(data, json_file)
