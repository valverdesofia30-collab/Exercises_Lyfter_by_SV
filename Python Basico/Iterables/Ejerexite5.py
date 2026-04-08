words= []
for word in range(5):
    word= input("Place your word:")
    words.append(word)
more_4_letters= [word for word in words if len(word) > 4]
print("Words with more than 4 letters are:", more_4_letters)