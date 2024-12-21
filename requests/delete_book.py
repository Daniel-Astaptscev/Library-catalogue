import sqlite3


def request(author: str, title: str) -> None:
    """
    Запрос на удаление книги по автору и названию.
            
    Args:
        author (str): автор книги.
        title (str): название книги.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM Books WHERE author = ? AND title = ?', (author, title))

    connection.commit()
    connection.close()
