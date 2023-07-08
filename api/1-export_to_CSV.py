#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/user/{}" \.format(user.id)
    todos_url = "https://jsonplaceholder.typicode.com/todos/{}" \.format(user_id)

    user_info = requests.request('GET', user_url).json()
    todo_info = requests.request('GET', todos_url).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj: (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    with open('{}.csv'.format(user_id), 'w') as cvsfile:
        csvwriter = csv.writer(csvfile, quoting=cvs.QUOTE_ALL)
        [csvwriter.writerow([user_id, user_info["username"], task["completed"], task["title"]]) for task in todos_info]
            
