def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError as ex:
            print(f"Invalid value:", ex)


def show_menu():
    print("\n1. Sum")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("6. Exit")


def sum(current, new):
    return current +  new
    

def subtract(current,new):
    return current - new
    

def multiplication(current, new):
    return current * new
    

def division(current, new):
    return current / new     

def reset_result():
    return 0
    

def calculator():
    current_number = get_number("Enter a number:")

    while True:
        show_menu()
        choice = input("Choose an option:")

        if choice == "1":
            new_number = get_number("Enter another number:")
            current_number = sum(current_number, new_number)
            print("Result:", current_number)
        elif choice == "2":
            new_number = get_number("Enter another number:")
            current_number = subtract(current_number, new_number)
            print("Result:", current_number)
        elif choice == "3":
            new_number = get_number("Enter another number:")
            current_number = multiplication(current_number, new_number)
            print("Result:", current_number)
        elif choice == "4":
            new_number = get_number("Enter another number:")
            try:
                current_number = division(current_number, new_number)
            except ZeroDivisionError as ex:
                print("Can´t be 0:", ex)
        elif choice == "5":
            current_number = reset_result() # pyright: ignore[reportUndefinedVariable]
            print("The result has been cleared", current_number)
        elif choice == "6":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

calculator()