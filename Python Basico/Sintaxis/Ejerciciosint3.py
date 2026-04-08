import random
secret_number = random.randint (1, 10)
while True:
    guess = int(input("Guess the secret number between 1 and 10"))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You have guessed the secret number")
        break
