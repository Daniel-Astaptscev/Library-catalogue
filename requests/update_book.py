import sqlite3

def request(author: str, title: str, state: int, status: int, masterpiece:
int, trash: int, book_id: int):
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

    cursor.execute(f'UPDATE Books SET author = ?, title = ?, state = ?, '
                   f'status = ?, masterpiece = ?, trash = ? WHERE id = ?', (author, title, state,
                                                   status, masterpiece,
                                                                            trash, book_id))

    connection.commit()
    connection.close()
