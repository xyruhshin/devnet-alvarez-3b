import requests
import random

API_URL = "https://pokeapi.co/api/v2/pokemon/"



def get_pokemon_data(name):
    try:
        response = requests.get(
            API_URL + name.lower(),
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()
        data = response.json()

        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"]
        }

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
        return None





pokemon_list = [
    "pikachu",
    "bulbasaur",
    "charmander",
    "squirtle",
    "eevee"
]

selected_pokemon = random.choice(pokemon_list)

pokemon = get_pokemon_data(selected_pokemon)


if pokemon:
    height = pokemon["height"] / 10
    weight = pokemon["weight"] / 10

    print("\n=== WHO'S THAT POKEMON? ===")
    print("Can you guess the Pokemon?")
    print("Height:", height, "meters")
    print("Weight:", weight, "kilograms")

    attempts = 3

    while attempts > 0:
        guess = input("\nEnter your guess: ").strip().lower()

        
        if not guess:
            print("Please enter a Pokemon name.")
            continue

        guessed_pokemon = get_pokemon_data(guess)

        if guessed_pokemon is None:
            print("Invalid Pokemon name. Try again.")
            continue
 
        if guess == pokemon["name"]:
            print("Correct! You guessed the Pokemon!")
            break
        else:
            attempts -= 1

            if attempts > 0:
                print("Wrong guess! Attempts remaining:", attempts)
            else:
                print("Game over!")
                print("The correct Pokemon was:",
                      pokemon["name"].title())


