"""
Midterm Practical Exam — Movie Collection Manager
Student: [Serrano, John Carlo S.]
"""
 
movies = [
    {
        "Movie Name": "The Shawshank Redemption",
        "Movie Status": "Watched"
    },
    {
        "Movie Name": "The Godfather",
        "Movie Status": "Watched"
    },
    {
        "Movie Name": "The Dark Knight",
        "Movie Status": "Unwatched"
    },
    {
        "Movie Name": "The Godfather Part II",
        "Movie Status": "Unwatched"
    }
]
 
 
def display_menu():
    print("\n=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View all Movies")
    print("3. Count watched vs unwatched")
    print("4. Find a Movie")
    print("5. Remove a Movie")
    print("6. Exit")
 
    return input("Choose an option: ")
 
 
def add_movie(movie_list):
    name = input("Movie Name: ")
    status = input("Movie Status (Watched/Unwatched): ")
 
    # Make the status consistent
    status = status.capitalize()
 
    movie_list.append({
        "Movie Name": name,
        "Movie Status": status
    })
 
    print(f"\n--- {name} added to list! ---")
 
 
def view_movies(movie_list):
    if not movie_list:
        print("\nNo movies in the collection.")
        return
 
    print("\n=== Movie List ===")
 
    for movie in movie_list:
        print(f"Movie Name: {movie['Movie Name']}")
        print(f"Movie Status: {movie['Movie Status']}")
        print("------------------------")
 
 
def count_watched_unwatched(movie_list):
    watched = 0
    unwatched = 0
 
    for movie in movie_list:
        if movie["Movie Status"].lower() == "watched":
            watched += 1
        elif movie["Movie Status"].lower() == "unwatched":
            unwatched += 1
 
    print("\n=== Movie Count ===")
    print(f"Watched: {watched}")
    print(f"Unwatched: {unwatched}")
 
    return watched, unwatched
 
 
def find_movie(movie_list):
    if not movie_list:
        print("\nNo movies found.")
        return
 
    search = input("Enter movie name to find: ").lower()
 
    found = False
 
    for movie in movie_list:
        if search in movie["Movie Name"].lower():
            print("\n=== Movie Found ===")
            print(f"Movie Name: {movie['Movie Name']}")
            print(f"Movie Status: {movie['Movie Status']}")
            found = True
 
    if not found:
        print("\nMovie not found.")
 
 
def remove_movie(movie_list):
    if not movie_list:
        print("\nNo movies to remove.")
        return
 
    name = input("Enter movie name to remove: ").lower()
 
    for movie in movie_list:
        if movie["Movie Name"].lower() == name:
            movie_list.remove(movie)
            print(f"\n--- {movie['Movie Name']} removed! ---")
            return
 
    print("\nMovie not found.")
 
 
def main():
    doing = True
 
    while doing:
        decision = display_menu()
 
        if decision == "1":
            add_movie(movies)
 
        elif decision == "2":
            view_movies(movies)
 
        elif decision == "3":
            count_watched_unwatched(movies)
 
        elif decision == "4":
            find_movie(movies)
 
        elif decision == "5":
            remove_movie(movies)
 
        elif decision == "6":
            doing = False
            print("\nThank you for using Movie Collection Manager!")
 
        else:
            print("\nInvalid option. Please choose 1-6.")
 
 
main()
