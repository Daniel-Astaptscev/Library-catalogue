import datetime

# def logger(type_error: str) -> None:
    #     """
    #     Запись в служебный лог-файл о произошедшей критической ошибки в ходе работы приложения.
    #
    #     Args:
    #         type_error (str): строковое обозначение сегмента ошибки для проверки при осуществлении записи в файл logs.txt.
    #     """
    #     now = datetime.datetime.now()
    #     with open('./logs.txt', 'a') as file:
    #         if type_error == 'AttributeError':
    #             file.write(
    #                 f"\n{now.strftime('%d-%m-%Y %H:%M')} == AttributeError: object has no attribute")
    #         elif type_error == 'ValueError':
    #             file.write(
    #                 f"\n{now.strftime('%d-%m-%Y %H:%M')} == ValueError: invalid literal for int()")
    #         else:
    #             pass
    # except ZeroDivisionError as e:
    #     logging.error(e)
