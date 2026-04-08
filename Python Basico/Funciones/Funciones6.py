def separate():
    food_list= "sushi-pizza-hot dog-fries"
    list= food_list.split("-")
    list.sort()
    result= "-".join(list)
    return result


print(separate())