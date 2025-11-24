# Simple Movie Collection Program (CRUD)

movies = []   # list to store movie records


def add_movie():
    print("\n--- Add a New Movie ---")
    title = input("Movie Name: ")
    year = input("Release Year: ")
    rating = input("Rating (out of 10): ")

    details = {
        "title": title,
        "year": year,
        "rating": rating
    }

    movies.append(details)
    print("Movie added!\n")


def show_movies():
    print("\n--- All Movies ---")
    if len(movies) == 0:
        print("No movies in the list.\n")
        return

    for i, m in enumerate(movies, start=1):
        print(f"{i}. {m['title']} ({m['year']}) - {m['rating']}/10")
    print()


def update_movie():
    print("\n--- Update Movie Info ---")
    show_movies()

    if len(movies) == 0:
        return

    try:
        num = int(input("Which movie number to update? ")) - 1
        if num < 0 or num >= len(movies):
            print("Invalid choice.\n")
            return
    except:
        print("Please enter a number.\n")
        return

    new_title = input("New name (leave empty to keep same): ")
    new_year = input("New year (leave empty to keep same): ")
    new_rating = input("New rating (leave empty to keep same): ")

    if new_title != "":
        movies[num]["title"] = new_title
    if new_year != "":
        movies[num]["year"] = new_year
    if new_rating != "":
        movies[num]["rating"] = new_rating

    print("Updated successfully!\n")


def delete_movie():
    print("\n--- Delete a Movie ---")
    show_movies()

    if len(movies) == 0:
        return

    try:
        num = int(input("Which movie number to delete? ")) - 1
        if num < 0 or num >= len(movies):
            print("Invalid choice.\n")
            return
    except:
        print("Please enter a valid number.\n")
        return

    movies.pop(num)
    print("Movie removed.\n")


def main_menu():
    while True:
        print("===== Movie Collection Menu =====")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_movie()
        elif option == "2":
            show_movies()
        elif option == "3":
            update_movie()
        elif option == "4":
            delete_movie()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


main_menu()