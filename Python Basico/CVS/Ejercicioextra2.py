import csv

file_name = "video_games.csv"


user_rating = input("Enter ESRB rating to search (E, T, M, etc.): ").upper()

found = False

with open(file_name, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
   
    next(reader)
    
    for row in reader:
        name, genre, developer, rating = row
        
        if rating.upper() == user_rating:
            print(f"\nName: {name}")
            print(f"Genre: {genre}")
            print(f"Developer: {developer}")
            print(f"Rating: {rating}")
            found = True


if not found:
    print("\nNo video games found with that ESRB rating.")