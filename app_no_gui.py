import json
import random


url = 'C:/Users/pc/OneDrive/Documentos/projet java/anime finder/anime_data.json'
with open(url, "r") as file:
    data = json.load(file)


def get_anime_by_name(name):
    name = name.lower()
    for anime in data:
        if anime["name"].lower() == name:
            return anime
    return None



def compare_two_animes(name1, name2):
    anime1 = get_anime_by_name(name1)
    anime2 = get_anime_by_name(name2)

    if not anime1 or not anime2:
        return None, None, "One or both anime not found!"

    if anime1["score"] > anime2["score"]:
        winner = anime1["name"]
    elif anime2["score"] > anime1["score"]:
        winner = anime2["name"]
    else:
        winner = "Tie"

    return anime1, anime2, winner

def get_anime_by_genre(genre_name):
    genre_name = genre_name.lower()
    results = []

    for anime in data:
        genres = [g.lower() for g in anime["genres"]]
        if genre_name in genres:
            results.append(anime)

    return results

def get_random_anime():
    return random.choice(data)
def random_anime_gui():
    anime = get_random_anime()
    

def display_anime(anime):
    print("\nName:", anime["name"])
    print("Episodes:", anime["episodes"])
    print("Score:", anime["score"])
    print("Genres:", ", ".join(anime["genres"]))
    print("Synopsis:", anime["synopsis"])
    print("Cover:", anime["img"])
    print("Status:", anime["status"])
    print("Year of Air:", anime["year"])


def check_anime_status(anime_name):
    anime = get_anime_by_name(anime_name)
    if not anime:
        return None
    else:
        print(f"Status of '{anime['name']}': {anime['status']}")




while True:
    print("\n-- Welcome to Anime Finder --")
    print("Please select your choice:")
    print("1. Search an anime")
    print("2. Compare two animes")
    print("3. Filter animes by genre")
    print("4. Choose a random anime to watch")
    print("5. Check anime status")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1-6.")
        continue

    if choice == 1:
        anime_name = input("Please enter an anime name: ")
        result = get_anime_by_name(anime_name)
        if result:
            display_anime(result)
        else:
            print("No anime found.")

    elif choice == 2:
        name1 = input("Enter first anime: ")
        name2 = input("Enter second anime: ")
        anime1, anime2, winner = compare_two_animes(name1, name2)

        if winner == "One or both anime not found!":
            print(winner)
        else:
            print("\n--- Anime 1 ---")
            display_anime(anime1)
            print("\n--- Anime 2 ---")
            display_anime(anime2)
            print("\nBetter anime:", winner)

    elif choice == 3:
        genre = input("Enter genre to filter: ")
        matches = get_anime_by_genre(genre)
        if matches:
            print(f"\nAnime in genre '{genre}':")
            for anime in matches:
                print(f"- {anime['name']} (Score: {anime['score']})")
        else:
            print(f"No anime found in genre '{genre}'.")

    elif choice == 4:
        random_anime = get_random_anime()
        print("\nRandom Anime Recommendation:")
        display_anime(random_anime)
    
    elif choice == 5:
        anime = input("Please enter anime name : ")
        check_anime_status(anime)

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter a number between 1-5.")
