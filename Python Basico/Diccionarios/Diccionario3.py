information_keys = ["name", "email"]
information_keys2 = {
    "name": "Sofia",
    "age": 26,
    "email": "valverdesofia30@gmail.com",
    "country": "Costa Rica"
}

for key in information_keys:
    if key in information_keys2:
        del information_keys2[key]
print(information_keys2)
