seconds = int(input("Enter the time in seconds:"))
if seconds >600:
    time = "greater"  # type: ignore
elif seconds <600:
    time = "lesser"  # type: ignore
else:
    seconds = 600
    time = "equal" # type: ignore
print(f"The seconds is {time} than 10 minutes")