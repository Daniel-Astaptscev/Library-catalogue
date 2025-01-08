import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import os
import logging

from requests import *
from ui_functions import *


class App(tk.Tk):
    """
    Основное применение - запуск и осуществление полного цикла работы приложения.

    Attributes:
        Представляют собой технические и стилевые характерики приложения при его запуске.

    Methods:
        create_main_menu: формирование основного пользовательского меню.
        create_tree_widget: формирование дерева записей приложения.
        create_progressbar: создание и заполнение шкалы прогресс-бара.
        item_selected: обработка выбора выделения строки в дереве записей.
        create_btn_find: действие при нажатии на кнопку -> найти книгу(и).
        create_btn_add: действие при нажатии на кнопку -> добавить книгу.
        create_btn_change: действие при нажатии на кнопку -> изменить книгу.
        create_btn_delete: действие при нажатии на кнопку -> удалить книгу.
        update_tree: действие при нажатии на кнопку -> обновить дерево записей.
        sort_column: выполнение сортировки дерева записей по столбцу.
        on_window_resize: обработка изменения размера progressbar при изменении окна приложения.
    """

    def __init__(self):
        super().__init__()
        self.title('Library catalogue')
        self.iconbitmap(default='./icons/favicon_main.ico')
        self.window_height = 860
        self.window_width = 1412
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self.window_width / 2))
        y_cordinate = int((screen_height / 2) - (self.window_height / 2))
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))

        self.flag_sort = True

        create_book.request()
        self.tree = self.create_tree_widget()
        self.menu = self.create_main_menu()
        self.progressbar = None
        self.progressbar = self.create_progressbar()

        self.bind('<Configure>', self.on_window_resize)

    def create_main_menu(self) -> tk.Menu:
        """
        Создание основного пользовательского меню с инструментами для осуществления дальнейшего взаимодействия пользователя с программой.

        Returns:
            сформированный объект класса tk -> меню.
        """
        menu = tk.Menu()
        menu.add_cascade(label='Обновить', command=self.update_tree)
        menu.add_cascade(label='Добавить книгу', command=self.create_btn_add)
        menu.add_cascade(label='Изменить книгу', command=self.create_btn_change)
        menu.add_cascade(label='Найти книгу', command=self.create_btn_find)
        menu.add_cascade(label='Удалить книгу', command=self.create_btn_delete)
        self.config(menu=menu)
        self.option_add('*tearOff', tk.FALSE)
        return menu

    def item_selected(self, event) -> list:
        """
        Обработка выделения строки в дереве записей приложения.

        Args:
            event: событие при выделении строки.

        Returns:
            select_item (list): список со всей информацией о выбранной книге.
        """
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            self.select_item = item['values']
            return self.select_item
        return ""

    def create_tree_widget(self, bd: list = None) -> ttk.Treeview:
        """
        Создание основного дерева с записями о книгах сформированного из базы данных.

        Args:
            bd (list): база данных которая используется для формирования дерева. По умолчанию используются все строки и столбцы из базы данных. При осуществлении пользовательского поиска получает через sql-запрос определённые строки и заполняет дерево согласно указанному условию.

        Returns:
            сформированный объект класса tk -> дерево записей.
        """
        style = ttk.Style()
        style.theme_use('winnative')
        style.configure('mystyle.Treeview.Heading', font=('Times New '
                                                          'Roman', 14, 'bold'))
        style.configure('mystyle.Treeview', font=('Times New Roman', 14))

        self.rowconfigure(index=2, weight=2)
        self.columnconfigure(index=0, weight=1)
        columns = ('column_1', 'column_2', 'column_3', 'column_4', 'column_5')
        self.tree = ttk.Treeview(columns=columns, show='headings', style='mystyle.Treeview')
        self.tree.grid(row=2, column=0, sticky='nsew')

        self.tree.heading('column_1', text='#', anchor='center')
        self.tree.heading('column_2', text='Автор', anchor='center', command=lambda: self.sort_column('author'))
        self.tree.heading('column_3', text='Название книги', anchor='center', command=lambda: self.sort_column('title'))
        self.tree.heading('column_4', text='Состояние', anchor='center', command=lambda: self.sort_column('state'))
        self.tree.heading('column_5', text='Статус', anchor='center')

        width_column_2, width_column_3 = select_book.request_max_len()

        self.tree.column('#1', stretch=tk.NO, width=40, anchor='center')
        self.tree.column('#2', stretch=tk.NO, width=width_column_2 * 9,
                         anchor='ne')
        self.tree.column('#3', stretch=tk.NO, width=width_column_3 * 10)
        self.tree.column('#4', stretch=tk.NO, width=110, anchor='center')
        self.tree.column('#5', stretch=tk.NO, width=80, anchor='center')

        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky='ns')

        self.tree.tag_configure('unread', background='#ecf2f9')
        self.tree.tag_configure('read', background='#9fbfdf')

        def insert_book(item: tuple) -> None:
            """
            Добавление всех полей с информацией о книге в дерерво записей. 

            Args:
                item (tuple): кортеж с информацией о книге.
            """
            book_state = ('✔' if item[3] == 1 else '')
            book_masterpiece = ('🏆' if item[5] == 1 else '')
            book_trash = ('♻' if item[6] == 1 else '')
            book_status = book_masterpiece + book_trash
            if item[4] == 1:
                self.tree.insert("", tk.END, values=(num, item[1], item[2], book_state, book_status), tags='read')
            else:
                self.tree.insert("", tk.END, values=(num, item[1], item[2], book_state, book_status), tags='unread')

        if type(bd) == list:
            for num, item in enumerate(bd, start=1):
                insert_book(item)
        else:
            for num, item in enumerate(select_book.request_sort('author', self.flag_sort), start=1):
                insert_book(item)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        return self.tree

    def on_window_resize(self, event) -> None:
        """
        Обработка изменения размера progressbar при изменении окна приложения.
        """
        if self.progressbar:
            width = self.winfo_width() if event is None else event.width
            self.progressbar.config(length=width - 4)

    def create_progressbar(self) -> None:
        """
        Создание и заполнение шкалы прогресс-бара в зависимости от кол-ва прочитанных книг из базы данных по отношению к их общему кол-ву.
        """
        maximum_value, current_value = select_book.request_sum()

        self.label_progressbar = ttk.Label(text=f'Прогресс чтения: {current_value} прочитно из {maximum_value}',
                                           font=('Times New Roman', 12, 'bold'))
        self.label_progressbar.grid(row=0, column=0, sticky='w')
        self.progressbar = ttk.Progressbar(orient='horizontal',
                                           maximum=maximum_value,
                                           value=current_value)
        self.progressbar.grid(row=1, column=0, sticky='ew')
        self.columnconfigure(0, weight=1)
        self.on_window_resize(None)

    # Метод для сортировки по убыванию и возрастанию
    ####################################################
    def sort_column(self, column: str) -> None:
        """
        Выполнение сортировки дерева записей по выбранному столбцу в зависимости от флага: по возрастанию или по убыванию. 

        Args:
            column (str): название столбца для осуществления сортировки.
        """
        if self.flag_sort:
            self.update_tree(bd=select_book.request_sort(column, self.flag_sort))
            self.flag_sort = False
        else:
            self.update_tree(bd=select_book.request_sort(column, self.flag_sort))
            self.flag_sort = True

    # Методы для работы с кнопками основного меню
    ####################################################
    def create_btn_find(self) -> None:
        """
        Запуск модального окна при взаимодействии пользователя с инструментом основного меню -> найти книгу(и).
        """
        modal_window = btn_find.ButtonFind()
        modal_window.add_window.wait_window()
        self.update_tree(bd=modal_window.result)

    def create_btn_add(self) -> None:
        """
        Запуск модального окна при взаимодействии пользователя с инструментом основного меню -> добавить книгу.
        """
        modal_window = btn_add.ButtonAdd()
        modal_window.add_window.wait_window()
        self.update_tree()

    def create_btn_change(self) -> None:
        """
        Запуск модального окна при взаимодействии пользователя с инструментом основного меню -> изменить книгу.
        """
        try:
            modal_window = btn_change.ButtonChange(self.select_item)
            modal_window.add_window.wait_window()
            py_logger.info(f'Book {self.select_item[1]} - {self.select_item[2]} has been successfully modified.')
            self.update_tree()
        except AttributeError as error:
            py_logger.warning('AttributeError ChangeBook', exc_info=True)
            showerror(title='Книга не выбрана', message='Ни одна книга не выбрана для изменения')

    def create_btn_delete(self) -> None:
        """
        Запуск диалогового окна при взаимодействии пользователя с инструментом основного меню -> удалить книгу.
        """
        try:
            delete_button = btn_delete.ButtonDelete(self.select_item)
            py_logger.info(f'Book {self.select_item[1]} - {self.select_item[2]} was successfully deleted.')
            if delete_button.result:
                self.update_tree()
        except AttributeError:
            py_logger.warning('AttributeError DeleteBook', exc_info=True)
            showerror(title='Книга не выбрана', message='Ни одна книга не выбрана для удаления')

    def update_tree(self, bd: list = None) -> None:
        """
        Удаление текущего дерева записей и формирование нового дерева записей с актуальными данными из базы данных через функцию -> create_tree_widget().

        Args:
            bd (list, optional): база данных которая используется для формирования дерева. По умолчанию используются все строки и столбцы из базы данных. При осуществлении пользовательского поиска получает через sql-запрос определённые строки и заполняет дерево согласно указанному условию.
        """
        [self.tree.delete(i) for i in self.tree.get_children()]
        self.tree = self.create_tree_widget(bd)


if __name__ == "__main__":
    if not os.path.isdir('data'):
        os.mkdir('data')

    # Формирование и запись логов в текстовый файл
    # получение пользовательского логгера и установка уровня логирования
    py_logger = logging.getLogger(__name__)
    py_logger.setLevel(logging.INFO)

    # настройка обработчика и форматировщика 
    py_handler = logging.FileHandler(f'./data/{__name__}.log', mode='a')
    py_formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

    # добавление форматировщика и обработчика к обработчику 
    py_handler.setFormatter(py_formatter)
    py_logger.addHandler(py_handler)

    app = App()
    app.mainloop()
