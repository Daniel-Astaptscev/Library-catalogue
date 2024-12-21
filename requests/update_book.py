import sqlite3


def request(author: str, title: str, state: int, status: int, masterpiece: int, trash: int, book_id: int) -> None:
    """
    Запрос на обновление информации о книге в базе данных.

    Args:
        author (str): автор книги.
        title (str): название книги.
        state (int): состояние книги.
        status (int): статус книги.
        masterpiece (int): шедевр ли книга.
        trash (int): макулатура ли книга.
        book_id (int): идентификатор книги в базе данных.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute(f'UPDATE Books SET author = ?, title = ?, state = ?, status = ?, masterpiece = ?, trash = ? WHERE id = ?',
                   (author, title, state, status, masterpiece, trash, book_id))

    connection.commit()
    connection.close()
