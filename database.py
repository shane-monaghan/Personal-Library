import sqlite3


def create_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books
                    (
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    progress TEXT NOT NULL
                    )
                    """)
    cursor.close()
    conn.close()


def add_entry(title, author, genre, progress):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    insert_tuple = (title, author, genre, progress)
    cursor.execute("""INSERT INTO books (title, author, genre, progress)
                   VALUES (?, ?, ?, ?)""", insert_tuple)
    conn.commit()
    cursor.close()
    conn.close()


def view_all():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()


def view_by(attribute, search):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    search_string = "%" + search + "%"
    cursor.execute("SELECT * FROM books WHERE " + attribute + " LIKE (?)", (search_string,))
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()



