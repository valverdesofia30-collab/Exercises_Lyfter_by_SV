import json

def read_pokemon(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    
        for i in data:
            if type(i["name"]) == dict:
                name = i["name"] ["english"]
    
            else:
                name = i["name"]
                
            if "base" in i:
                attack = i["base"]["Attack"]
                defense = i["base"]["Defense"]
                speed = i["base"]["Speed"]
                print(f"Name: {name}, Attack: {attack}, Defense: {defense}, Speed: {speed}")
                
            else:
                print(f"Name: {name} (No stats available)")
                
read_pokemon("pokemon.json", indent=4)