import sqlite3

def request(book_author: str, book_title: str):
    """
    ???
            
    Args:
        book_id (int, optional): столбец для уникального идентификационного номера.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM Books WHERE author = ? AND title = ?', (book_author, book_title))

    connection.commit()
    connection.close()
