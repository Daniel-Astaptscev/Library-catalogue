import sqlite3

def request(book_author: str, book_title: str, book_year: int) -> list:
    """           
    Args:
        book_author (str, optional): столбец для автора книги.
        book_title (str, optional): столбец для названия книги.
        book_year (int, optional): столбец для года издания книги.

    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Books WHERE author = ? OR title = ? OR year = ?', (book_author, book_title, book_year))
    books = cursor.fetchall()
            
    connection.commit()
    connection.close()

    return books
