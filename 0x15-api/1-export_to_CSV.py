#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{base_url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(
        f"{base_url}todos", params={"userId": user_id}).json()
    file = f"{user_id}.csv"

    with open(file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for todo in todos:
            writer.writerow([user_id, username,
                            todo.get("completed"), todo.get("title")])
