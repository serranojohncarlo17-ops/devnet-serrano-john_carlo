"""
Midterm Practical Exam — Movie Collection Manager
Student: [Serrano, John Carlo S.]
"""

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


def display_menu():
    print("--movie list--")

    print("\n=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View all Movies")
    print("3. Count watched vs unwatched")
    print("4. Find a Movie")
    print("5. Remove a Movie")
    print("6. Exit")

    return input("Choose an option: ")
pass


def add_movie(movie_list):
    name = input("Name: ")
    status = input("Movie Status: ")
    movie_list.append({"Name": name, "Status": status})
    searched = name.capitalize()
    print(f"\n--- {searched} added to list! ---")
    pass


def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    if not movie_list:
        print("No movie found.")
        return
    for movies in movie_list:
        print(f"  {movies['Movie Name']}: {movies['Movie Status']}")
    pass



doing = True

while doing == True:
    decision = display_menu()
    if decision == 1:
        movies = add_movie(movies)
    if decision == 2:
        movies = view_movies(movies)
    elif decision == 6:
        doing = False



def main():

    doing = True

while doing == True:
    decision = display_menu()
    if decision == 1:
        movies = add_movie(movies)
    if decision == 2:
        movies = view_movies(movies)
    elif decision == 6:
        doing = False
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()

