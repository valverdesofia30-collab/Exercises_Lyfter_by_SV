import json

def get_pokemon (file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    pokemon_name = input("Enter the name of the Pokemon: ")
    pokemon_level = int(input("Enter the level of the Pokemon: "))
    pokemon_type = input("Enter the type of the Pokemon: ")
    
    new_pokemon = {
        "name": pokemon_name, 
        "level": pokemon_level, 
        "type": pokemon_type 
    }

    data.append(new_pokemon)
    with open(file_path,"w", encoding="utf-8")as file:
        json.dump(data, file, indent=4)
    print("Pokemon added successfully!")
    
get_pokemon("pokemon.json")  