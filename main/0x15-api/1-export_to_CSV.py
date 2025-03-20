#!/usr/bin/python3
"""
module contains a Python script to export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users/{employee_id}").json()
    completed_params = {"userId": employee_id, "completed": "true"}
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()
    complete = requests.get(f"{url}todos", params=completed_params).json()
    file_name = f"{employee_id}.csv"

    new_list = []
    for val in todos:
        data = []
        data.append(val.get("userId"))
        data.append(users.get("username"))
        data.append(val.get("completed"))
        data.append(val.get("title"))
        new_list.append(data)

    with open(file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(new_list)
