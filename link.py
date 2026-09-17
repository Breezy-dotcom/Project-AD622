import requests
import csv

url = "http://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
data = response.json()

with open("todos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(["userId", "id", "title", "completed"])

    for item in data:
        writer.writerow([
            item["userId"],
            item["id"],
            item["title"],
            item["completed"]
        ])

    print("The file 'todos.csv' was created successfully")
