
def display_menu(movie_list):
    print("--movie list--")
    display_movie(movie_list)

    print("\n=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View all Movies")
    print("3. Count watched vs unwatched")
    print("4. Find a Movie")
    print("5. Remove a Movie")
    print("6. Exit")

    return input("Choose an option: ")

def display_movie(movie_list):
    if not movie_list:
        print("No contacts found.")
        return
    for movies in movie_list:
        print(f"  {movies['Title']}: {movies['Movie Status']}")

def add_movie(movie_list):
    name = input("Movie Name: ")
    status = input("Movie Status: ")
    movie_list.append({"Movie Name": name, "Movie Status": status})
    searched = name.capitalize()
    print(f"\n--- {searched} added to Movie List! ---")

def del_movie(movie_list):
    name = input("Name to delete: ")
    if not movie_list:
        print("No movies found.")
        return

    found = any(c["Name"].lower() == name.lower() for c in movie_list) # Looks through list, if one matches name it outputs true, woooow
    if not found:
        print(f"\n--- No contact named '{name.capitalize()}' found. ---")
        return

    movie_list[:] = [c for c in movie_list if c["Movie Name"].lower() != name.lower()]
    print(f"\n--- {name.capitalize()} Deleted from Movie List! ---")

def display_main(movie_list):
    while True:
        choice = display_menu(movie_list)
        if choice == "1":
            add_movie(movie_list)
        elif choice == "2":
            del_movie(movie_list)
        elif choice == "3":
            print("\n=== Exiting Movie List ===")
            break
        else:
            print("Invalid option. Please choose 1-3.")
    return movie_list

if __name__ == "__main__":
    display_main()


