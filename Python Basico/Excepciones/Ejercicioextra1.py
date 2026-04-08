def name():
    try:
        full_name = str(input("Enter your your name:"))
    
        if full_name.isdigit():
            raise ValueError("The name cannot contain numbers")
        
        age = input("Enter your age:")
        age = int(age)

        print(f"Hello {full_name}, your age is {age}")

    except ValueError as error:
        print("Invalid:", error)

if __name__ == "__main__":
    name()

