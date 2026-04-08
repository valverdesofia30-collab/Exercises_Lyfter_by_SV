my_favorite_netflix_series = "Rick and Morty"
for char in my_favorite_netflix_series:
    print(char)

my_favorite_color = "Blue"
for color in range(len(my_favorite_color)):
    print(my_favorite_color[color])

food = "Sushi"
reversed_word= ""
for index in range(len(food)-1, -1, -1):
    reversed_word += food[index]+"\n"
print(reversed_word)