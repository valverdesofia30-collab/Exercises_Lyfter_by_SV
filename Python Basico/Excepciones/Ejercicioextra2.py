def number(list):
    print("Result:")

    for i in list:
        try:
            num = int(i)
            print(i, "converted to", num)
        except ValueError:
            print(f"{i} cannot be converted to an integer")

my_list  = ["4", "hola", "10", "5.2"]
number(my_list)