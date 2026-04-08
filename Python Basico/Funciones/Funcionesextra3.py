def count_vowels(word):
    count_vowels= 0
    vowels= ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for Q in word:
        if Q in vowels:
            count_vowels += 1
    return count_vowels

word= input("Enter a word:")

print(count_vowels(word))