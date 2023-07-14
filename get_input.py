from os import system, name


# For adding a book entry
def get_title():
    title = ""
    while title.strip() == "":
        title = input("Enter the book's title: ")
    return title


def get_author():
    author = ""
    while author.strip() == "":
        author = input("Enter the book's author: ")
    return author


def get_genre():
    genre = ""
    genre_dict = {
        "1": "Non-fiction",
        "2": "Fiction",
        "3": "Historical Fiction",
        "4": "Mystery",
        "5": "Science Fiction",
        "6": "Fantasy",
        "7": "Horror",
        "8": "Classics"
    }
    for key in genre_dict.keys():
        print(key + ". " + genre_dict[key])
    while genre not in genre_dict.keys():
        genre = input("Enter the number of the book's genre: ")
        genre = genre.strip()
    genre = genre_dict[genre]
    return genre


def get_progress():
    progress = ""
    progress_dict = {
        "1": "Finished",
        "2": "In progress",
        "3": "DNF",
        "4": "TBR"
    }
    for key in progress_dict.keys():
        print(key + ". " + progress_dict[key])
    while progress not in progress_dict.keys():
        progress = input("Enter the number of the book's current status: ")
        progress = progress.strip()
    progress = progress_dict[progress]
    return progress


# Continue option
def get_continue():
    to_continue = ""
    print("1.", "Continue")
    print("2.", "Return to menu")
    while to_continue != "1" and to_continue != "2":
        to_continue = input("Enter the number of what you would like to do: ")
        to_continue = to_continue.strip()
    if to_continue == "1":
        return True
    return False


# For the main menu
def get_menu_choice():
    choice = ""
    choices = ["1", "2", "3", "4", "5"]
    print("1.", "Add a Book")
    print("2.", "Search for a Book")
    print("3.", "Update a Book")
    print("4.", "Delete a Book")
    print("5.", "Quit")
    while choice not in choices:
        choice = input("Enter the number of what you would like to do: ")
        choice = choice.strip()
    return choice


# For searching for books
def get_category():
    category = ""
    category_dict = {"1":"title",
                     "2":"author",
                     "3":"genre",
                     "4":"progress"
                     }
    print("1.", "Title")
    print("2.", "Author")
    print("3.", "Genre")
    print("4.", "Book Status")
    while category not in category_dict.keys():
        category = input("Enter the number of what you'd like to search by: ")
        category = category.strip()
    return category_dict[category]


def get_search():
    search = ""
    search = input("Enter your search, enter nothing to view all: ")
    return search


# Clears the screen in between actions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

