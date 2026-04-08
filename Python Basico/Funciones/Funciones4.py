def text():
    first_text= "Hello Daniel"
    reversed_text= ""
    
    
    for message in first_text:
        reversed_text= message + reversed_text
    
    return reversed_text


print(text())