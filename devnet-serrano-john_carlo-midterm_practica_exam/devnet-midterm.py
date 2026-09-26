import search, addel

def choice():
    print("\n=== Movie List ===")
    search.display_menu(movies)

    print("\n=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View all Movies")
    print("3. Count watched vs unwatched")
    print("4. Find a Movie")
    print("5. Remove a Movie")
    print("6. Exit")
    decision = int(input("Choose an option: "))
    return decision


movies = [
    {
        "Movie Name" : "The Shawshank Redemption",
        "Movie Status" : "Watched"
    },

    {
        "Name" : "The Godfather",
        "Movie Status" : "watched"
    },

    {
        "Name" : "The Dark Knight",
        "Movie Status" : "Unwatched"
    },
    {
        "Name" : "The Godfather Part II",
        "Movie Status" : "Unwatched"
    }
]

doing = True

while doing == True:
    decision = choice()
    if decision == 1:
        movies = addel.display_main(movies)
    elif decision == 2:
        search.display_main(movies)
    elif decision == 3:
        doing = False
