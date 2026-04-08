with open("input.txt", "r") as file:
    words = []
    
    for line in file:
        words.append(line.strip())

text = " ".join(words)

with open("output.txt", "w") as output_file:
    output_file.write(text)
    
print("File created successfully")