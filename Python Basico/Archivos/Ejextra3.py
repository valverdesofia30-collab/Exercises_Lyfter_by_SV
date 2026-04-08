text = input("Enter a line of text:")

with open("text.txt", "a") as file:
    file.write(text + "\n")
    
print("The text was added to the end of the file")