numbers = input("Enter the list of numbers")
user_list = [int(num) for num in numbers.split()]
serch_number = int(input("Enter the number you want to look for"))
count = user_list.count(serch_number)
print(f"The number {serch_number} is {count} times in the list.")
