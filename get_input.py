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
    while genre.strip() not in genre_dict.keys():
        genre = input("Enter the number of the book's genre: ")
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
    while progress.strip() not in progress_dict.keys():
        progress = input("Enter the number of the book's genre: ")
    progress = progress_dict[progress]
    return progress
