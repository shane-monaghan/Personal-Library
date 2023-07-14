from database import *
from get_input import *


def main_menu():
    clear()
    choice = get_menu_choice()
    if choice == "1":
        get_entry_input()
    elif choice == "2":
        search_book()

def get_entry_input():
    clear()
    title = get_title()
    author = get_author()
    print("Genres")
    genre = get_genre()
    print("Book Status")
    progress = get_progress()
    print("")
    add_entry(title, author, genre, progress)
    print("Would you like to continue adding books?")
    if get_continue():
        get_entry_input()
    else:
        main_menu()


def search_book():
    clear()
    print("Attributes")
    category = get_category()
    print("Search")
    search = get_search()
    clear()
    if search == "":
        view_all()
    else:
        view_by(category, search)
    print("")
    if get_continue():
        search_book()
    else:
        main_menu()


main_menu()
view_all()