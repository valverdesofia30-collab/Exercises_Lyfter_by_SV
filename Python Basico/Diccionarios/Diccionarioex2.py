employees = [
    {"name": "Alice", "email": "alice@gmail.com", "department": "HR"},
    {"name": "Bob", "email": "bob@gmail.com", "department": "IT"},
    {"name": "Carlos", "email": "carlos@gmail.com", "department": "Finance"},
    {"name": "Diana", "email": "diana@gmail.com", "department": "HR"},
]

result = {}
for employee in employees:
    department = employee["department"]

    if department not in result:
        result[department] = []
    result[department].append(employee)
print(result)
