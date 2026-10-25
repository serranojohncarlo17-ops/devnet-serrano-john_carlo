
import requests
import random


pokenumber = random.randint(1, 5)


if pokenumber == 1:
    url1 = "https://pokeapi.co/api/v2/pokemon/pikachu"
elif pokenumber == 2:
    url1 = "https://pokeapi.co/api/v2/pokemon/charizard"
elif pokenumber == 3:
    url1 = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
elif pokenumber == 4:
    url1 = "https://pokeapi.co/api/v2/pokemon/squirtle"
else:
    url1 = "https://pokeapi.co/api/v2/pokemon/lapras"



x = requests.get(url1, headers={"User-Agent": "Mozilla/5.0"})



if x.status_code == 200:
    data = x.json()


    name = data["name"]
    height = data["height"]
    weight = data["weight"]



    print("=== POKEMON GUESSING GAME ===")
    print("Guess the Pokemon!")
    print("You have 3 attempts.\n")
    
    print("Pokemon choices:")
    print("1. Pikachu")
    print("2. Charizard")
    print("3. Bulbasaur")
    print("4. Squirtle")
    print("5. Lapras\n")

    
    print("Height:", height / 10, "meters")
    print("Weight:", weight / 10, "kilograms")



    for attempt in range(1, 4):
        guess = input(f"\nAttempt {attempt}/3: ").lower().strip()

        if guess == "pikachu":
            url2 = "https://pokeapi.co/api/v2/pokemon/pikachu"
        elif guess == "charizard":
            url2 = "https://pokeapi.co/api/v2/pokemon/charizard"
        elif guess == "bulbasaur":
            url2 = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
        elif guess == "squirtle":
            url2 = "https://pokeapi.co/api/v2/pokemon/squirtle"
        elif guess == "lapras":
            url2 = "https://pokeapi.co/api/v2/pokemon/lapras"
        else:
            print("Invalid Pokemon name!")
            continue



        y = requests.get(url2, headers={"User-Agent": "Mozilla/5.0"})



        if y.status_code == 200:
            answer = y.json()



            if answer["name"] == name:
                print("Correct! You guessed the Pokemon!")
                break
            else:
                print("Wrong guess! Try again.")
                
                
                
        else:
            print("Error retrieving Pokemon data.")

    else:
        print("\nGame over! The Pokemon was", name.title())


else:
    print("Error retrieving Pokemon data.")
    print("Status code:", x.status_code)
