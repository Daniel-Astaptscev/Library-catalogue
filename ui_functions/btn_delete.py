import datetime
from requests import delete_book
from tkinter.messagebox import showerror, showinfo, askyesno

class ButtonDelete:

    def __init__(self, book_id):
        self.book_id = book_id
        self.result = askyesno(title='Удаление книги из библиотеки',
                          message='Подтвердить удаление?')

        if self.result:
            try:
                delete_book.request(self.book_id)
            except:
                showerror(title='Ошибка', message='Ни одна книга не '
                                                  'выбрана\nСделана запись в лог-файл')
                #return logging(type_error='AttributeError')
                #self.update_tree()
                showinfo('Результат', 'Операция подтверждена', icon='info')
            else:
                showinfo('Результат', 'Операция подтверждена', icon='warning')






    # elif btn_name == 'btn_find':
    #     add_window.title('Найти книгу')
    #     add_window.iconbitmap('./assets/icons/favicon_find.ico')
    #     label_status.destroy()
    #     combobox_status.destroy()
    #     label_text = ttk.Label(add_window,
    #                            text='необходимо выбрать и заполнить ОДНО поле по которому будет осуществляться поиск книги',
    #                            font=('Times New Roman', 10),
    #                            background='white', wraplength=350,
    #                            justify=tk.CENTER)
    #     label_text.place(x=61, y=154)
    #     btn_submit = ttk.Button(add_window, text='Найти книгу',
    #                             command=action)
    # elif btn_name == 'btn_change':
    #     add_window.title('Изменить книгу')
    #     add_window.iconbitmap('./assets/icons/favicon_change.ico')
    #     btn_submit = ttk.Button(add_window, text='Изменить книгу',
    #                             command=action)
    #
    #     # Проверка осуществлен ли выбор любой строки для изменения или
    #     # удаления
    #     try:
    #         entry_author.insert(0, self.select_item[1])
    #         entry_title.insert(0, self.select_item[2])
    #         spinbox_year.insert(0, self.select_item[3])
    #         combobox_status.set('В наличии' if self.select_item[
    #                                                4] == 'В наличии' else 'Выдана')
    #     except:
    #         showerror(title='Ошибка',
    #                   message='Ни одна книга не выбрана\nСделана запись в лог-файл')
    #         add_window.destroy()
    #         return logging(type_error='AttributeError')


# def action():
#             """
#             В зависимости от типа кнопки выбранной пользователем в
#             основном меню - реализуется запрос через класс Request в файле
#             sql_requests.py к базе данных.
#
#             Returns:
#                 showerror (func, optional): запуск диалогового окна при
#                 возникновении ошибки не являющейся критической.
#
#                 logging (func, optional): при получении ошибки в ходе
#                 операции производит запуск функции осуществляющей её запись в
#                 текстовый файл.
#             """
#             book_author = entry_author.get()
#             book_title = entry_title.get()
#             book_year = spinbox_year.get()
#
#             if btn_name == 'btn_find':
#                 self.update_tree(
#                     sql_requests.where.connection_with_request(book_author,
#                                                                book_title,
#                                                                book_year))
#                 add_window.destroy()
#                 return None
#
#             select_status = combobox_status.get()
#             book_status = f'{1 if select_status == "В наличии" else 0}'
#
#             # Проверка блока на заполнение всех полей
#             if (len(book_author) == 0 or len(book_title) == 0 or len(
#                     book_year) == 0 or len(
#                 select_status) == 0) and btn_name != 'btn_find':
#                 return showerror(title='Ошибка',
#                                  message='Не все поля заполнены')
#
#             # Проверка блока на ошибку при вводе в поле вместо цифр для года - буквы или другие знаки
#             try:
#                 if btn_name == 'btn_add':
#                     sql_requests.update.connection_with_request(book_author,
#                                                                 book_title,
#                                                                 int(book_year),
#                                                                 int(book_status))
#                 elif btn_name == 'btn_change':
#                     book_id = self.select_item[0]
#                     sql_requests.update.connection_with_request(book_author,
#                                                                 book_title,
#                                                                 int(book_year),
#                                                                 int(book_status),
#                                                                 book_id)
#             except:
#                 showerror(title='Ошибка',
#                           message='Нельзя указывать никакие другие символы в поле "год" кроме цифр\nСделана запись в лог-файл')
#                 return logging(type_error='ValueError')
#
#             add_window.destroy()



            

