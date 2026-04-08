import csv
import os

file_name = "video_games.csv"

file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["name", "genre", "developer", "rating"])
    
    while True:
        try:        
            n = int(input("How many video games do you want to enter: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(n): # pyright: ignore[reportUndefinedVariable]
        print(f"\nVideo Game {i+1}:")
        
        name = input("Enter name: ")
        genre = input("Enter genre: ")
        developer = input("Enter developer: ")
        rating = input("Enter ESRB rating: ")
        
        writer.writerow([name, genre, developer, rating]) # type: ignore
        
print("\nData successfully saved in video_games.csv")