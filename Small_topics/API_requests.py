# Application Programming Interface 

import requests
import json 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
    url = f"{base_url}pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Info on pokemon found!")
        pokemon_data = response.json()
        print(f"pokemon_data: {pokemon_data}")
        return pokemon_data
    else:
        print("Info on pokemon was not found!")
        return None

# should have no whitespaces at back and front and should be lower 
pokemon = input("What is your fav pokemon: ").strip().lower()
pokemon_info = get_pokemon_info(pokemon)

print(f"Name: {pokemon_info["name"]}")
file_path_pokemon = "python_learning/small_topics/pokemon.json"
filttered_data = {
    "name": pokemon_info["name"],
    "id": pokemon_info["id"],
    "height": pokemon_info["height"],
    "weight": pokemon_info["weight"],
    "types": [t["type"]["name"] for t in pokemon_info["types"]],
}
try:
    with open(file_path_pokemon, mode="w") as file:
        json.dump(filttered_data, file, indent=4)
except FileNotFoundError:
    print("file was not found!")
finally:
    print("Success")
    file.close()

