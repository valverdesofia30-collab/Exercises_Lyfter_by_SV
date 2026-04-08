import csv

def genre(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        genre_count ={}
        for row in reader:
            genre = row[1]
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        print(f"Genre founds: ")
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")
        
genre("video_games.csv") # type: ignore