import sqlite3

def request(book_author: str, book_title: str, book_year: int, book_status: int, book_id: int):
    """
    ???
            
    Args:
        book_author (str): столбец для автора книги.
        book_title (str): столбец для названия книги.
        book_year (int): столбец для года издания книги.
        book_status (int): столбец для указания статуса книги.
        book_id (int): столбец для уникального идентификационного номера.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute(f'UPDATE Books SET author = ?, title = ?, year = ?, status = ? WHERE id = ?', (book_author, book_title, book_year, book_status, book_id))

    connection.commit()
    connection.close()
