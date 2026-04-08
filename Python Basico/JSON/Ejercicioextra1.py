import json

def read_pokemon(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
        for i in data:
            print(f"Name: {i['name']}, Level {i['level']}, Type: {i['type']}")


read_pokemon("pokemon.json")