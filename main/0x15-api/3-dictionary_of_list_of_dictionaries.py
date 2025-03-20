#!/usr/bin/python3
"""
module contains a Python script to export data in the JSON format
"""
import csv
import json
import requests



if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users/").json()    
    complete = requests.get(f"{url}todos", params=completed_params).json()

    file_name = "todo_all_employees.json"

    new_list = []
    data = {}
    for val in todos:
        completed_params = {"userId": "id", "completed": "true"}
        todos = requests.get(f"{url}todos", params={"userId": "id"}).json()
        new_list.append({
                "username": users.get("username"),
                "task": val.get("title"),
                "completed": val.get("completed"),})


    with open(file_name, "w", newline='') as json_file:
        json.dump(data, json_file)
