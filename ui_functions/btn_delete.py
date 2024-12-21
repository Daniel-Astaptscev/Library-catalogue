from requests import delete_book
from tkinter.messagebox import showinfo, askyesno


class ButtonDelete:
    """
    Формирование диалогового окна удаления книги из библиотеки и осуществление запроса в случае подтверждения.

    Attributes:
        select_item (list): список с информацией об авторе и названии выбранной книги.
    """

    def __init__(self, select_item):
        self.author = select_item[1]
        self.title = select_item[2]

        self.result = askyesno(title='Удаление книги из библиотеки', message='Подтвердить удаление?')

        if self.result:
            delete_book.request(self.author, self.title)
            showinfo("Результат", "Операция подтверждена")
        else:
            showinfo("Результат", "Операция отменена")
