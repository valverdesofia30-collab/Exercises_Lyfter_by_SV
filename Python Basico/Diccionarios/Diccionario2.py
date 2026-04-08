information1 = ["first_name", "last_name", "age", "country"]
information2 = ["Sofia", "Valverde", 26, "Costa Rica"]

dictionary = {}

for i in range(len(information1)):
    dictionary[information1[i]] = information2[i]

print(dictionary)