import json

def get_pokemon (file_path):
    with open(file_path, "r", encoding="utf-8")as file:
        data = json.load(file)
        
        pokemon_type = input("Enter the type of the pokemon you want to search: ")
        found_pokemon = [pokemon for pokemon in data if pokemon["type"][0].lower() == pokemon_type.lower()]
    
        if not found_pokemon:
            print("No pokemon found if this type.")
            
        else:
            print(f"The pokemon of this type are: ")
            for pokemon in found_pokemon:
                print(pokemon['name'])
        
        
get_pokemon("pokemon.json")