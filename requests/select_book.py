import sqlite3

def request_sum() -> tuple:
    """
    ???

    Returns:
        len_sum_all, len_sum_state (tuple): формируется список из кортежа ???
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(id) FROM Books')
    book = cursor.fetchall()
    len_sum_all = book[0][0]

    cursor.execute('SELECT COUNT(id) FROM Books WHERE state = 1')
    book = cursor.fetchall()
    len_sum_state = book[0][0]

    connection.commit()
    connection.close()

    return (len_sum_all, len_sum_state)


def request_max_len() -> tuple:
    """
    ???

    Returns:
        len_author, len_title (tuple): формируется список из кортежа ???
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


def request_sort(item_sort: str, sorting: bool) -> list:
    """
    ???

    Args:
        item_sort (str): ???

    Returns:
        books (list): формируется список из кортежей/а в каждом из которых вся информация по книге/ам
    """
    connection = sqlite3.connect('./data/books.db')
    cursor = connection.cursor()

    if sorting:
        cursor.execute(f'SELECT * FROM Books ORDER BY {item_sort} ASC')
    else:
        cursor.execute(f'SELECT * FROM Books ORDER BY {item_sort} DESC')
    book = cursor.fetchall()

    connection.commit()
    connection.close()

    return book
