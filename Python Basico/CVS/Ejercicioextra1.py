import csv

file_name = "video_games.csv"

with open(file_name, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    next(reader)
    
    for row in reader:
        name, genre, developer, rating = row
        print(f"Name: {name}")
        print(f"Genre: {genre}")
        print(f"Developer: {developer}")
        print(f"Rating: {rating}")
        print()