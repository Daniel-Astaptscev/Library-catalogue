# О проекте

**Проект представляет** собой независимое приложение для работы с каталогом (книжный) и имеет фиксированный набор необходимых инструментов.

**Проект реализован** на языке программирования `Python 3.9` с использованием возможностей языка запросов `SQL` для хранения данных в удобном формате, а именно в форме базы данных. 

**Основной алгоритм работы приложения** - это набор операций выполняемых в `main.py` осуществляющих обращение к `sql_requests.py` который непосредственно выполняет `sql` запросы к базе данных через `sqlite3`, а затем полученные результаты возвращает исполняемому приложению для отображения их конечному пользователю. 

Программа полностью стабильна. 

### Отметки о выполнении требований к проекту

| Выполнение  | Описание            
| ----------------- | ----------------- | ------------------------------------------------------------------ |
| ✅ | через основное меню и отдельное модальное окно осуществляется удобное управление книгами |
| ✅ | реализация хранения данных в формате .bd с помощью sql |
| ✅ | используются только стандартные библиотеки имеющиеся в Python 3.9 |
| ✅ | использование классов и отдельных от main файлов .py |
| ✅ | обработка ошибок осуществлена через конструкцию try-except в тех блоках, где они могут возникнуть, а также их логирование в отдельный текстовый файл .txt |
| ✅ | для каждой операции есть свой тип запроса в sql реализованный в отдельном классе .py |
| ✅ | добавлен docstring для классов и функций, а также отдельные комментарии по структуре |
| ✅ | аннотирование функций и переменных в коде |


## Используемые инструменты

Языки программирования:

- python 3.9
- sql

Стандартные библиотеки:

- tkinter
- sqlite3


## Интерфейс

```
  Пользовательское меню содержит несколько инструментов для взаимодействия с программой
```

| Функция | Описание |
| :-------- | :------------------------- |
| `Добавить` | **Автоматическое обновление дерева записей при изменении**. Заполните основные поля для добавления книги в базу данных. |
| `Изменить` | **Автоматическое обновление дерева записей при изменении**. Выберите строку с любой книгой, а затем измените необходимые поля для перезаписи информации в базе данных. |
| `Удалить` | **Автоматическое обновление дерева записей при изменении**. Выберите строку с любой книгой для её удаления из базы данных. |
| `Найти` | **Автоматическое обновление дерева записей при нахождении**. Заполните необходимое поле для поиска нужной книги или книг в базе данных для их отображения |
| `Обновить` | **Возвращение к отображению актуального дерева записей**. Обновите информацию в дереве записей согласно изменениям в базе данных. |


## База данных

| Столбец             | Описание                                                               |
| ----------------- | ------------------------------------------------------------------ |
| id | **Integer, Primary Key**. Уникальный идентификационный номер. |
| author | **Text, Not null**. Указывается автор книги. |
| title | **Text, Not null**. Указывается название книги. | |
| year | **Integer, Not null**. Указывается год издания книги. | |
| status | **Integer, Not null**. Указывается статус книги в каталоге. | |


## Развёртывание проекта

Для запуска проекта никаких дополнительных загрузок и установок модулей, библиотек - не предусмотрено. Настройка не требуется. 

Осуществление запуска:

```console
  python main.py
```


## Папки и Файлы проекта

**main.py** - файл инициализации приложения.

**** - основные ресурсы приложения.

**** - основные файлы для работы приложения.

**library.db** - служебный файл являющийся основной базой данных для приложения.

**** - служебный файл для осуществления запросов к базе данных в ходе работы приложения.

**/logs.txt** - текстовый файл для записи отчётов по ошибкам в ходе работы приложения.

**icons** - графические файлы приложения в виде иконок.

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)


## Разработчик

- [@daniel-astaptscev](https://github.com/Daniel-Astaptscev)