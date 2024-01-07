#!/usr/bin/python3
"""Returns information about employee's todo list progress"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base_url}users/{sys.argv[1]}").json()
    todos = requests.get(f"{base_url}todos", params={"userId": sys.argv[1]}).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed")]
    print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)})")

    for c in completed:
        print(f"\t {c}")

