import tkinter as tk
import os
from tkinter import ttk
from tkinter.messagebox import showwarning

from requests import *
from ui_functions import *

class App(tk.Tk):
    """
    Основное применение - запуск и осуществление полного цикла работы приложения.

    Attributes:
        Представляют собой технические и стилевые характерики приложения при его запуске.

    Methods:
        create_main_menu: формирование основного пользовательского меню
        create_tree_widget: формирование дерева записей приложения
        item_selected: обработка выбора выделения строки в дереве записей
        btn_add: действие при нажатии на кнопку -> добавить книгу
        btn_change: действие при нажатии на кнопку -> изменить книгу
        btn_find: действие при нажатии на кнопку -> найти книгу
        btn_delete: действие при нажатии на кнопку -> удалить книгу
        update_tree: действие при нажатии на кнопку -> обновить дерево записей
        ???
    """

    def __init__(self):
        super().__init__()
        self.title('Library catalogue')
        self.iconbitmap(default='./icons/favicon_main.ico')
        self.window_height = 860
        self.window_width = 1240
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))   

        create_book.request()
        self.tree = self.create_tree_widget()
        self.menu = self.create_main_menu()
        self.progressbar = self.create_progressbar()


    def create_progressbar(self):
        """
        ???
        """
        maximum_value, current_value = select_book.request_sum()

        label_progressbar = ttk.Label(text=f'Прогресс чтения: {current_value} прочитно из {maximum_value}', font=('Times New Roman', 12, 'bold'))
        label_progressbar.grid(row=0, column=0, sticky='w')
        progressbar = ttk.Progressbar(orient='horizontal',
                                      length=self.window_width,
                                      maximum=maximum_value,
                                      value=current_value)
        progressbar.grid(row=1, column=0, sticky='n')

    def create_main_menu(self):
        """
        Создание основного пользовательского меню с инструментами для осуществления дальнейшего взаимодействия пользователя с программой.

        Returns:
            сформированный объект класса tk -> меню.
        """
        menu = tk.Menu()
        menu.add_cascade(label='Обновить', command=self.update_tree)
        menu.add_cascade(label='Добавить книгу', command=btn_add.ButtonAdd)
        menu.add_cascade(label='Изменить книгу', command=self.btn_change)
        menu.add_cascade(label='Найти книгу', command=self.btn_find)
        menu.add_cascade(label='Удалить книгу', command=self.btn_delete)
        self.config(menu=menu)
        self.option_add('*tearOff', tk.FALSE)
        return menu

    def item_selected(self, event):
        """
        Обработка выделения строки в дереве записей приложения

        Args:
            event: событие при выделении строки
        """
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            self.select_item = item['values']
        return self.select_item

    def create_tree_widget(self, bd: list = None):
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
        self.tree.heading('column_2', text='Автор', anchor='center')
        self.tree.heading('column_3', text='Название книги', anchor='center')
        self.tree.heading('column_4', text='Состояние', anchor='center')
        self.tree.heading('column_5', text='Статус', anchor='center')

        width_column_2, width_column_3 = select_book.request_max_len()

        self.tree.column('#1', stretch=tk.NO, width=40, anchor='center')
        self.tree.column('#2', stretch=tk.NO, width=width_column_2*9,
                         anchor='ne')
        self.tree.column('#3', stretch=tk.NO, width=width_column_3*10)
        self.tree.column('#4', stretch=tk.NO, width=110, anchor='center')
        self.tree.column('#5', stretch=tk.NO, width=80, anchor='center')

        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky='ns')

        if type(bd) == list:
            if len(bd) == 0:
                showwarning(title='Ошибка', message='Данная книга/и не найдена в базе данных')

            for item in bd:
                if item[4] == 1:
                    self.tree.insert("", tk.END, values=(
                        item[0], item[1], item[2], item[3], 'В наличии'))
                else:
                    self.tree.insert("", tk.END, values=(
                        item[0], item[1], item[2], item[3], 'Выдана'))
        else:
            for item in select_book.request_all():
                if item[4] == 1:
                    self.tree.insert("", tk.END, values=(
                        item[0], item[1], item[2], item[3], 'В наличии'))
                else:
                    self.tree.insert("", tk.END, values=(
                        item[0], item[1], item[2], item[3], 'Выдана'))

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        return self.tree

    # Методы для работы с кнопками основного меню
    ####################################################
    def btn_change(self) -> None:
        """
        Запуск модального окна при взаимодействии пользователя с инструментом основного меню -> изменить книгу.
        """
        button_change = btn_change.ButtonChange(self.select_item)

    def btn_find(self) -> None:
        """
        Запуск модального окна при взаимодействии пользователя с инструментом основного меню -> найти книгу.
        """
        pass

    def btn_delete(self):
        """
        Запуск диалогового окна при взаимодействии пользователя с инструментом основного меню -> удалить книгу.

        Returns:
            logging (func, optional): при получении ошибки в ходе операции производит запуск функции осуществляющей её запись в текстовый файл.
        """
        button_delete = btn_delete.ButtonDelete(self.select_item[0])

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
        logs_file = open('./data/logs.txt', 'w')

    app = App()
    app.mainloop()
