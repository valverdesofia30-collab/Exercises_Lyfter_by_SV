def sort_songs(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            songs = file.readlines()

        songs = [song.strip() for song in songs]
        songs.sort()

        with open(output_file, "w", encoding="utf-8") as file:
            for song in songs:
                file.write(song + "\n")

        print("Songs sorted and saved successfully.")
    
    except FileNotFoundError:
        print("The input file was not found.")

def main():
    input_file = "songs.txt"
    output_file = "sorted_songs.txt"

    sort_songs(input_file, output_file)

if __name__ == "__main__":
    main()