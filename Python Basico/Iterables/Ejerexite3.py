numbers= [25, 30, 45, 60, 90, 120]
minor= float("inf")
for num in numbers:
    if num < minor:
        minor = num 
print("The minor number is:", minor)