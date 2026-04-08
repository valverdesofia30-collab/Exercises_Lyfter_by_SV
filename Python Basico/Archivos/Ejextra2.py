def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read()
        new_line_count = lines.split()
        new_line_count_2 = len(new_line_count)
    print(f"This file has {new_line_count_2} words")


count_words("original.txt")