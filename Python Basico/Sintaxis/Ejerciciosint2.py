name = str(input("Enter your first name"))
last_name =str(input("Enter your last name"))
age = int(input("Enter your age"))
if age <=2:
    stage = "baby"
elif age <=11:
    stage = "child"
elif age <=12:
    stage = "preteen"
elif age <=17:
    stage = "teen"
elif age <29:
    stage = "young adult"
elif age <=59:
    stage = "adult"
else:
    stage = "older adult"
print (f"Your full name is {name} {last_name} and you are {stage}")