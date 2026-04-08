import json

def get_pokemon (file_path):
    
    with open(file_path, "r", encoding="utf-8")as file:
        data = json.load(file)
        types = {}
        
        for i in data:
            pokemon_types = i["type"]
            pokemon_level = i["level"]
            
            if isinstance(pokemon_types, str):
                pokemon_types = [pokemon_types]
                
            for pokemon_type in pokemon_types:
                
                if pokemon_type not in types:
                    types[pokemon_type] = []
                    
                types[pokemon_type].append(pokemon_level)
                
        for pokemon_type, levels in types.items():
            average = sum(levels) / len(levels)
            print(f"Type: {pokemon_type}")
            print(f"Average level: {average}")
            
get_pokemon("pokemon.json")