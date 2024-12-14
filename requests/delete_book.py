import sqlite3

def request(book_id: int):
    """
    ???
            
    Args:
        book_id (int, optional): столбец для уникального идентификационного номера.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM Books WHERE id = {book_id}')

    connection.commit()
    connection.close()
