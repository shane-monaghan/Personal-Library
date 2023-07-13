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
        progress = input("Enter the number of the book's genre: ")
        progress = progress.strip()
    progress = progress_dict[progress]
    return progress


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


