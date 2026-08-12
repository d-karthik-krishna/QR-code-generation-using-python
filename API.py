# how we can connect to a API using python
# link = https://pokeapi.co/api/v2/

import requests

baseURL = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{baseURL}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Searching for the pokemon......\n")
        pokemon_data = response.json()
        return pokemon_data
        
    else :
        print(f"Search Failed! {response.status_code}")

pokemon_name = input("Enter the pokemon name: ").lower()
get_pokemon_info = get_pokemon_info(pokemon_name)

if get_pokemon_info:
    print(f"Name : {get_pokemon_info["name"].upper()}\nID : {get_pokemon_info["id"]}\nHeight : {get_pokemon_info["height"]}inches\nWeight : {get_pokemon_info["weight"]}kgs")