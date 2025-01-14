import tkinter as tk
from tkinter import ttk
from requests import where_book
from ui_functions import window_center, logger
from tkinter.messagebox import showwarning


class ButtonFind:
    """
    Создание модального окна поиска книги(и).

    Attributes:
        Представляют собой технические и стилевые характерики модального окна при его запуске.

    Methods:
        create_window: формирование основного модального окна.
        action: выполнение действий при нажатии на кнопки -> найти книгу(и).
    """

    def __init__(self):
        self.add_window = tk.Toplevel()
        self.add_window.title('Найти книгу(и)')
        self.add_window.geometry('610x280')
        self.add_window.iconbitmap('./icons/favicon_find.ico')
        self.result = []

        window_center.center(self.add_window)
        self.create_window()

    def create_window(self):
        """
        Создание основного модального окна с полями ввода и кнопкой "найти книгу(и)".
        """
        label_author = ttk.Label(self.add_window, text='Автор:',
                                 font=('Georgia', 14))
        label_author.place(x=66, y=20)
        self.entry_author = ttk.Entry(self.add_window, font=('Georgia', 14), width=30)
        self.entry_author.place(x=140, y=20)

        label_title = ttk.Label(self.add_window, text='Название:',
                                font=('Georgia', 14))
        label_title.place(x=34, y=60)
        self.entry_title = ttk.Entry(self.add_window, font=('Georgia', 14), width=30)
        self.entry_title.place(x=140, y=60)

        label_state = ttk.Label(self.add_window, text='Состояние:',
                                font=('Georgia', 14))
        label_state.place(x=30, y=104)
        state = ['Прочитано', 'Не прочитано']
        combobox_state = ttk.Combobox(self.add_window, values=state)
        combobox_state.place(x=140, y=110)

        label_status = ttk.Label(self.add_window, text='Наличие:',
                                 font=('Georgia', 14))
        label_status.place(x=326, y=105)
        status = ['В библиотеке', 'Отсутствует']
        combobox_status = ttk.Combobox(self.add_window, values=status)
        combobox_status.place(x=420, y=110)

        answer = ['Да', 'Нет']
        label_masterpiece = ttk.Label(self.add_window, text='Шедевр:',
                                      font=('Georgia', 14))
        label_masterpiece.place(x=51, y=150)
        combobox_masterpiece = ttk.Combobox(self.add_window, values=answer)
        combobox_masterpiece.place(x=140, y=155)

        label_trash = ttk.Label(self.add_window, text='Макулатура:',
                                font=('Georgia', 14))
        label_trash.place(x=300, y=150)
        combobox_trash = ttk.Combobox(self.add_window, values=answer)
        combobox_trash.place(x=420, y=155)

        def selected_state(event):
            self.select_state = combobox_state.get()

        def selected_status(event):
            self.select_status = combobox_status.get()

        def selected_masterpiece(event):
            self.select_masterpiece = combobox_masterpiece.get()

        def selected_trash(event):
            self.select_trash = combobox_trash.get()

        combobox_state.bind('<<ComboboxSelected>>', selected_state)
        combobox_status.bind('<<ComboboxSelected>>', selected_status)
        combobox_masterpiece.bind('<<ComboboxSelected>>',
                                  selected_masterpiece)
        combobox_trash.bind('<<ComboboxSelected>>', selected_trash)

        btn_submit = ttk.Button(self.add_window, text='Найти книгу(и)',
                                command=self.action)
        btn_submit.place(x=260, y=218)

    def action(self):
        """
        Выполнение действий при нажатии на кнопку "найти книгу(и)": получение значений из полей ввода и запрос на
        поиск книг(и) в базе данных.
        """
        author = self.entry_author.get().strip()
        title = self.entry_title.get().strip()
        state = getattr(self, 'select_state', None)
        status = getattr(self, 'select_status', None)
        masterpiece = getattr(self, 'select_masterpiece', None)
        trash = getattr(self, 'select_trash', None)

        fields = {
            'author': author,
            'title': title,
            'state': '1' if state == "Прочитано" else ('0' if state == "Не прочитано" else None),
            'status': '1' if status == "В библиотеке" else ('0' if status == "Отсутствует" else None),
            'masterpiece': '1' if masterpiece == "Да" else ('0' if masterpiece == "Нет" else None),
            'trash': '1' if trash == "Да" else ('0' if trash == "Нет" else None)
        }

        fields = {k: v for k, v in fields.items() if v}

        if not fields:
            logger.add_log('the text in the field is empty', 'find')
            return

        self.result = where_book.request(**fields)
        if self.result:
            self.add_window.destroy()
        else:
            showwarning(title='Ошибка', message='Данная книга/и не найдена в базе данных')
            self.add_window.destroy()
