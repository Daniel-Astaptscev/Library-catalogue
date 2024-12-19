import sqlite3

def request(**book_parameters: dict) -> list:
    """           
    Args:
        book_parameters (dict): ???
    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    query = "SELECT * FROM Books WHERE "

    books_find = []
    for key, value in book_parameters.items():
        query += f"{key} = ?"
        query += " AND "
        books_find.append(value)
    # удаление последнего "AND" из запроса
    query = query[:-4]

    cursor.execute(query, tuple(books_find))
    books = cursor.fetchall()
            
    connection.commit()
    connection.close()

    return books
