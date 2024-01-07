#!/usr/bin/python3
"""Exports all employee data in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    file = "todo_all_employees.json"
    all_data = {}
    users = requests.get(f"{base_url}users").json()

    for user in users:
        user_id = user["id"]
        todos = requests.get(
            f"{base_url}todos", params={"userId": user_id}).json()
        all_data[user_id] = [{
            "username": user["username"],
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in todos]

    with open(file, "w") as jsonfile:
        json.dump(all_data, jsonfile)
