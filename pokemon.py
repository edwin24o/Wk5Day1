# TASK 1
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def display_pokemon_info(pokemon_data):
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Pokémon: {name.capitalize()}")
    print("Abilities:", ", ".join(abilities))

if __name__ == "__main__":
    pokemon_name = "pikachu"
    pokemon_data = fetch_pokemon_data(pokemon_name)
    display_pokemon_info(pokemon_data)

print('=' * 60)

# TASK 2
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def calculate_average_weight(pokemon_data_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_data_list)
    return total_weight / len(pokemon_data_list)

def display_pokemon_info(pokemon_data):
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    weight = pokemon_data['weight']
    print(f"Pokémon: {name.capitalize()}")
    print("Abilities:", ", ".join(abilities))
    print(f"Weight: {weight}")

if __name__ == "__main__":
    pokemon_names = ["venusaur", "charizard", "blastoise"]
    pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

    for pokemon_data in pokemon_data_list:
        display_pokemon_info(pokemon_data)
        print()

    average_weight = calculate_average_weight(pokemon_data_list)
    print(f"Average Weight: {average_weight}")
