import requests

def fetch_pokemon_data(pokemon_name):
    """
    Fetches data for a given Pokémon from the Pokémon API.

    Args:
        pokemon_name (str): The name of the Pokémon to fetch data for.

    Returns:
        dict: The Pokémon's data, or None if there was an error.
    """
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return None
    except Exception as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None

def calculate_average_weight(pokemon_list):
    """
    Calculates the average weight of Pokémon in the list.

    Args:
        pokemon_list (list): The list of Pokémon data.

    Returns:
        float: The average weight.
    """
    valid_pokemon = [pokemon for pokemon in pokemon_list if pokemon]
    if not valid_pokemon:
        print("No valid Pokémon to calculate average weight.")
        return 0
    total_weight = sum(pokemon['weight'] for pokemon in valid_pokemon)
    return total_weight / len(valid_pokemon)

# Pokémon names to fetch
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# Fetch data and display results
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    if pokemon:
        name = pokemon['name']
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Name: {name}, Abilities: {abilities}")

# Calculate and display average weight
average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight} units")

# Existing code (fetching Pokémon data and calculating average weight)...

# New functionality to save data to a file
with open("pokemon_data.txt", "w") as file:
    for pokemon in pokemon_data:
        if pokemon:
            file.write(f"Name: {pokemon['name']}, Abilities: {', '.join(ability['ability']['name'] for ability in pokemon['abilities'])}\n")
    file.write(f"\nAverage Weight: {average_weight} units\n")

print("Pokémon data has been saved to 'pokemon_data.txt'.")
# Save Pokémon data to a file
with open("pokemon_data.txt", "w") as file:
    for pokemon in pokemon_data:
        if pokemon:
            name = pokemon['name']
            abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
            file.write(f"Name: {name}, Abilities: {', '.join(abilities)}\n")
    file.write(f"\nAverage Weight: {average_weight} units\n")

print("Pokémon data has been saved to 'pokemon_data.txt'.")

import requests  # Importing the requests library

# === Function Definitions ===
def fetch_pokemon_data(pokemon_name):
    """
    Fetches data for a given Pokémon from the Pokémon API.

    Args:
        pokemon_name (str): The name of the Pokémon to fetch data for.

    Returns:
        dict: The Pokémon's data, or None if there was an error.
    """
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return None
    except Exception as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None

def calculate_average_weight(pokemon_list):
    """
    Calculates the average weight of Pokémon in the list.

    Args:
        pokemon_list (list): The list of Pokémon data.

    Returns:
        float: The average weight.
    """
    valid_pokemon = [pokemon for pokemon in pokemon_list if pokemon]
    if not valid_pokemon:
        print("No valid Pokémon to calculate average weight.")
        return 0
    total_weight = sum(pokemon['weight'] for pokemon in valid_pokemon)
    return total_weight / len(valid_pokemon)

# === Task 1: Setting up Virtual Environment and Installing Packages ===
# (No code needed here. You’ve already completed this by setting up your virtual environment
# and installing the 'requests' library.)

print("=== Task 1: Virtual Environment Setup ===")
print("Virtual environment successfully set up and 'requests' library installed.")

# === Task 2: Fetch and display data for Pikachu ===
print("\n=== Task 2: Pikachu Data ===")
pikachu = fetch_pokemon_data("pikachu")
if pikachu:
    name = pikachu['name']
    abilities = [ability['ability']['name'] for ability in pikachu['abilities']]
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")

# === Task 3: Multiple Pokémon Analysis ===
print("\n=== Task 3: Multiple Pokémon Data ===")
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

# Display Pokémon details
for pokemon in pokemon_data:
    if pokemon:
        name = pokemon['name']
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Name: {name}, Abilities: {', '.join(abilities)}")

# Calculate and display average weight
average_weight = calculate_average_weight(pokemon_data)
print(f"\nAverage Weight: {average_weight} units")
