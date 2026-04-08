def count_character (text, char):
    count_char= 0
    for Q in text:
        if Q == char:
            count_char += 1

    return count_char


text= input("Enter a text:")
char= input("Enter a character to count:")
print(count_character(text, char))