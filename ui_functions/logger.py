import datetime
from tkinter.messagebox import showerror

def add_log(type_error: str, show_messege) -> None:
    with open("./data/logs.txt", "a") as file:
        dt = datetime.datetime.now()
        file.write(f'{dt:%d}.{dt:%m}.{dt:%y} {dt:%H:%M:%S}: {type_error}\n')

    if show_messege == 'delete':
        return showerror(title="Книга не выбрана", message="Ни одна книга не выбрана для удаления")
    elif show_messege == 'change_choice':
        return showerror(title="Книга не выбрана", message="Ни одна книга не выбрана для изменения")
    elif show_messege == 'add':
        return showerror(title="Не все поля заполнены", message="Заполните все поля для добавления книги в библиотеку")
    elif show_messege == 'change':
        return showerror(title="Не все поля заполнены", message="Заполните все поля для изменения книги в библиотеке")
    