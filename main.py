from database import *
from get_input import *


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


get_entry_input()
view_all()