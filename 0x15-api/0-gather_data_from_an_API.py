import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Get employee information
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
user_response = requests.get(user_url)

if user_response.status_code != 200:
    print(f"User with ID {employee_id} not found")
    sys.exit(1)

user_data = user_response.json()
employee_name = user_data["name"]

# Get all tasks
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_response = requests.get(todos_url)

if todos_response.status_code != 200:
    print("Failed to retrieve tasks")
    sys.exit(1)

todos = todos_response.json()

# Filter tasks by employee_id and completed status
employee_tasks = [todo for todo in todos if todo["userId"] == employee_id]

completed_tasks = [task for task in employee_tasks if task["completed"]]
total_tasks = len(employee_tasks)

# Display results
completed_count = len(completed_tasks)

print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")

for task in completed_tasks:
    print(f"\t {task['title']}")

