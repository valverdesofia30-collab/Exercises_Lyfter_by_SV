def count_character (word, char):
    result= []
    for Q in word:
        if len(Q) > char:
            result.append(Q)
    return result


word= input("Enter the list of words:")
word= word.split(",")
char= int(input("Enter the minimal letters in the words:"))
print(count_character(word,char))