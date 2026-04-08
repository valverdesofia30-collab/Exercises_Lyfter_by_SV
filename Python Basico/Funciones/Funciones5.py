def my_favorite_restaurant():
    uppercase_count= 0
    lowercase_count= 0
    restaurant= "I love Today Sushi"
    for i in restaurant:
        if i.isupper():
            uppercase_count += 1
        elif i.islower():
            lowercase_count += 1
    

    print(f"The count of uppercase are:", uppercase_count)
    print(f"The count of lowercase are:", lowercase_count)


my_favorite_restaurant()