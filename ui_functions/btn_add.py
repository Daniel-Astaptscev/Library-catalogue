import tkinter as tk
from tkinter import ttk
from requests import insert_book
from ui_functions import window_center, logger


class ButtonAdd:
    """
    Создание модального окна добавления книги.

    Attributes:
        Представляют собой технические и стилевые характерики модального окна при его запуске.

    Methods:
        create_window: формирование основного модального окна.
        action: выполнение действий при нажатии на кнопки -> добавить книгу.
    """

    def __init__(self):
        self.add_window = tk.Toplevel()
        self.add_window.title('Добавить книгу')
        self.add_window.geometry('610x280')
        self.add_window.iconbitmap('./icons/favicon_add.ico')

        window_center.center(self.add_window)
        self.create_window()

    def create_window(self) -> None:
        """
        Создание основного модального окна с полями ввода и кнопкой "добавить книгу".
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

        btn_submit = ttk.Button(self.add_window, text='Добавить книгу',
                                command=self.action)
        btn_submit.place(x=260, y=218)

    def action(self) -> None:
        """
        Выполнение действий при нажатии на кнопку "добавить книгу": получение значений из полей ввода и запрос на
        добавление книги в базу данных.
        """
        author = self.entry_author.get()
        title = self.entry_title.get()
        try:
            state = f'{1 if self.select_state == "Прочитано" else 0}'
            status = f'{1 if self.select_status == "В библиотеке" else 0}'
            masterpiece = f'{1 if self.select_masterpiece == "Да" else 0}'
            trash = f'{1 if self.select_trash == "Да" else 0}'
        except AttributeError as error:
            logger.add_log(error, 'add')
        else:
            if len(author) != 0 and len(title) != 0:
                insert_book.request(author, title, state, status, masterpiece, trash)
                self.add_window.destroy()
            else:
                logger.add_log('the text in the field is empty', 'add')
