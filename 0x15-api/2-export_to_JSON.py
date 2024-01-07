#!/usr/bin/python3
"""Exports employee data in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{base_url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(
        f"{base_url}todos", params={"userId": user_id}).json()
    file = f"{user_id}.json"

    with open(file, "w") as jsonfile:
        json.dump({user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        } for todo in todos]}, jsonfile)
