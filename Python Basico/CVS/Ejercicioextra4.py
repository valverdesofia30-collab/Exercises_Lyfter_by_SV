import csv

def get_developer(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        choose_developer = input("Place the developer that you want: ")
        for row in reader:
            developer = row[2]
            if choose_developer == developer:
                name = row[0]
                genre = row[1]
                rating = row[3]
                print(f"{name}: {rating}: {genre}:")
                
get_developer("video_games.csv")