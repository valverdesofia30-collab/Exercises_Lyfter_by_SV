products = [
    {"name": "Monitor", "category": "Electronics", "price": 300},
    {"name": "Body Lotion", "category": "Personal Care", "price": 400},
    {"name": "Keyboard", "category": "Electronics", "price": 150},
    {"name": "Shampoo", "category": "Personal Care", "price": 400},
]

result = {}
for product in products:
    category = product["category"]
    price = product["price"]
    if category not in result: 
        result[category] = 0
    result[category] += price
    result[category] += price
print(result)
