from database import *
from get_input import *


def get_entry_input():
    title = get_title()
    author = get_author()
    genre = get_genre()
    progress = get_progress()
    add_entry(title, author, genre, progress)