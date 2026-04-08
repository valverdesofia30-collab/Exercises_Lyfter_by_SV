def sum_values(list):
    count = 0

    for Q in list:
        try:
            number = float(Q)
            count += number
            print(number, "the sum is correct")
        except ValueError:
            print(f"Invalid value: {Q}")

    print("The total sum is:", count)

my_list = ["10", "apple", "5.5", "3", "n/a"]
sum_values(my_list)