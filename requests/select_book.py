import sqlite3

def request_all() -> list:
    """
    ???
            
    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()

    connection.commit()
    connection.close()

    return books


def request_sum() -> list:
    """
    ???

    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    # cursor.execute('PRAGMA table_info("Books")')
    # column_names = [i[1] for i in cursor.fetchall()]
    # print(column_names)

    cursor.execute('SELECT COUNT(id) FROM Books')
    book = cursor.fetchall()
    len_sum_all = book[0][0]

    cursor.execute('SELECT COUNT(id) FROM Books WHERE presence = 1')
    book = cursor.fetchall()
    len_sum_state = book[0][0]

    connection.commit()
    connection.close()

    return (len_sum_all, len_sum_state)


def request_max_len() -> list:
    """
    ???

    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('SELECT MAX(LENGTH(author)), MAX(LENGTH(title)) FROM '
                   'Books')
    book = cursor.fetchall()
    len_author = book[0][0]
    len_title = book[0][1]

    connection.commit()
    connection.close()

    return (len_author, len_title)
