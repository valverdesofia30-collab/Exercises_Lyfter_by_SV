sales = [
    {
        "date": "24/01/2026",
        "customer_name": "Vicente Fernandez",
        "items": [
            {
                "name": "Laptop",
                "upc": "ITEM-001",
                "price": 1200
            },
            {
                "name": "Mouse",
                "upc": "ITEM-002",
                "price": 2500
            },
            {
                "name": "Keyboard",
                "upc": "ITEM-003",
                "price": 3000
            }
        ]
    },
    {
            "date": "25/01/2026",
            "customer_name": "Pedro Infante",
            "items": [
                {
                    "name": "Laptop",
                    "upc": "ITEM-001",
                    "price": 1200
                },
                {
                    "name": "Monitor",
                    "upc": "ITEM-004",
                    "price": 3500
                }
        ]
    },
    {
        "date": "26/01/2026",
        "customer_name": "Juan Gabriel",
        "items": [
            {
                "name": "Monitor",
                "upc": "ITEM-004",
                "price": 3500
            },
            {
                "name": "Mouse",
                "upc": "ITEM-002",
                "price": 2500
            },
            {
                "name": "Cellphone",
                "upc": "ITEM-005",
                "price": 1500
            }
        ]
    }
]

result = {}
for sale in sales:
    for item in sale ["items"]:
        upc = item["upc"]
        price = item["price"]
        if upc in result:
            result[upc] += price
        else:
            result[upc] = price
print(result)