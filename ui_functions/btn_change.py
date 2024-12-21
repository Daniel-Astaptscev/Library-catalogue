import tkinter as tk
from tkinter import ttk
from requests import where_book, update_book
from ui_functions import window_center, logger


class ButtonChange:
    """
    Создание модального окна изменения книги.

    Attributes:
        Представляют собой технические и стилевые характерики модального окна при его запуске.

    Methods:
        create_window: формирование основного модального окна.
        action: выполнение действий при нажатии на кнопки -> изменить книгу.
    """

    def __init__(self, select_item):
        self.author = select_item[1]
        self.title = select_item[2]
        self.book = where_book.request(author=self.author, title=self.title)[0]

        self.add_window = tk.Toplevel()
        self.add_window.title('Изменить книгу')
        self.add_window.geometry('610x280')
        self.add_window.iconbitmap('./icons/favicon_change.ico')

        window_center.center(self.add_window)
        self.create_window()

    def create_window(self):
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

        self.entry_author.insert(0, self.book[1])
        self.entry_title.insert(0, self.book[2])
        combobox_state.set('Прочитано' if self.book[3] == 1 else 'Не прочитано')
        combobox_status.set('В библиотеке' if self.book[4] == 1 else 'Отсутствует')
        combobox_masterpiece.set('Да' if self.book[5] == 1 else 'Нет')
        combobox_trash.set('Да' if self.book[6] == 1 else 'Нет')

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

        btn_submit = ttk.Button(self.add_window, text='Изменить книгу',
                                command=self.action)
        btn_submit.place(x=260, y=218)

    def action(self):
        author = self.entry_author.get()
        title = self.entry_title.get()
        try:
            state = f'{1 if self.select_state == "Прочитано" else 0}'
            status = f'{1 if self.select_status == "В библиотеке" else 0}'
            masterpiece = f'{1 if self.select_masterpiece == "Да" else 0}'
            trash = f'{1 if self.select_trash == "Да" else 0}'
        except AttributeError as error:
            logger.add_log(error, 'change')
        else:
            if len(author) != 0 and len(title) != 0:
                update_book.request(author, title, state, status, masterpiece, trash, self.book[0])
                self.add_window.destroy()
            else:
                logger.add_log('the text in the field is empty', 'change')
