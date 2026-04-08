my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in my_list if num % 2 == 0] # pyright: ignore[reportUndefinedVariable]
print(even_numbers)

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in list_numbers if num % 2 == 1]
print(odd_numbers)