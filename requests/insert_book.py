import sqlite3

def request(author: str, title: str, state: int, status: int, masterpiece: int, trash: int):
    """
    ???
            
    Args:
        author (str): столбец для автора книги.
        title (str): столбец для названия книги.
        state (int): ???.
        status (int): ???.
        masterpiece (int): ???.
        trash (int): ???.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Books (author, title, state, status, '
                    'masterpiece, trash) VALUES (?, ?, ?, ?, ?, ?)',
                   (author, title, state, status, masterpiece, trash))

    connection.commit()
    connection.close()
