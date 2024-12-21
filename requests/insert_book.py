import sqlite3


def request(author: str, title: str, state: int, status: int, masterpiece: int, trash: int) -> None:
    """
    Запрос на добавление новой книги в базу данных.
            
    Args:
        author (str): автор книги.
        title (str): название книги.
        state (int): состояние книги.
        status (int): статус книги.
        masterpiece (int): шедевр ли книга.
        trash (int): макулатура ли книга.
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Books (author, title, state, status, '
                   'masterpiece, trash) VALUES (?, ?, ?, ?, ?, ?)',
                   (author, title, state, status, masterpiece, trash))

    connection.commit()
    connection.close()
