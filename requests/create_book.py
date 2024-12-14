import sqlite3

def request():
    """
    ???
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        author TEXT NOT NULL,
        title TEXT NOT NULL,
        state INTEGER NOT NULL,
        status INTEGER NOT NULL,
        masterpiece INTEGER NOT NULL,
        trash INTEGER NOT NULL)''')

    connection.commit()
    connection.close()
