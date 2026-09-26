# This is menu brooo
def display_menu(movie_list):
    print("\n=== Contact List ===")
    display_movie(movie_list)

    print("\n=== List Menu ===")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Name (Z-A)")
    print("3. Sort by Phone Number")
    print("4. Search by Name")
    print("5. Exit")
    return input("Choose(1-5): ")

# Core functions stuff
def sort_by_name(movies, reverse=False):
    return sorted(movies, key=lambda x: x["Name"].lower(), reverse=reverse)

def sort_by_phone(movies):
    return sorted(movies, key=lambda x: x["Contact Number"])

def search_by_name(movies, query):
    results = [c for c in movies if query.lower() in c["Name"].lower()]
    return results if results else None

def display_movie(movie_list):
    if not movie_list:
        print("No contacts found.")
        return
    for contact in movie_list:
        print(f"  {contact['Name']}: {contact['Contact Number']}")

# Main loop
def display_main(movie_list:dict):
    while True:
        choice = display_menu(movie_list)
        
        if choice == "1":
            sorted_contacts = sort_by_name(movie_list)
            print("\n--- Sorted by Name (A-Z) ---")
            display_movie(sorted_contacts)
            print("--- Sorted by Name (A-Z) ---")
        elif choice == "2":
            sorted_contacts = sort_by_name(movie_list, reverse=True)
            print("\n--- Sorted by Name (Z-A) ---")
            display_movie(sorted_contacts)
            print("--- Sorted by Name (Z-A) ---")
        elif choice == "3":
            sorted_contacts = sort_by_phone(movie_list)
            print("\n--- Sorted by Phone Number ---")
            display_movie(sorted_contacts)
            print("--- Sorted by Phone Number ---")
        elif choice == "4":
            search_query = input("Enter name to search: ")
            results = search_by_name(movie_list, search_query)
            if results:
                print(f"\n--- Search Results for '{search_query}' ---")
                display_movie(results)
                print(f"--- Search Results for '{search_query}' ---")
            else:
                print(f"\n--- No contacts found matching '{search_query}' ---")
        elif choice == "5":
            print("\n=== Exiting Movie List... ===")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    display_main()
