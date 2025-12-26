

"""
Реализовать функцию с названием task_1.
Функция принимает на вход 4 значения. left_r: int, right_r: int,
 string_for_processing: str, default_max_r: int = 3

Функция должна возвращать значение в соответствии со следующей логикой:
1. Слева и справа должны быть удалены символы табуляции.
2. Слева и справа должны быть удалены символы в количестве left_r и right_r соответственно,
если они меньше default_max_r. В противном случае удалить дефолтное количество символов.
"""

def task_1(
    left_r: int,
    right_r: int,
    string_for_processing: str,
    default_max_r: int = 3
) -> str:

    """
    :param left_r: количество символов для удаления слева
    :param right_r: количество символов для удаления справа
    :param string_for_processing: входная строка для обработки
    :param default_max_r: максимально допустимое количество удаленных символов
    :return: обработанная строка
    """

    clean = string_for_processing.strip("\t") # удаляется ТОЛЬКО табуляция
    left = min(left_r, default_max_r)
    right = min(right_r, default_max_r)

    result = clean[left:]
    if right > 0:
        result = result[:-right]

    return result


# Примеры
print(task_1(7, 0, "\t  Привет мир!  \t", 7))
print(task_1(0, 3, "   Питухон   ", 2))
print(task_1(0, 0, "\tТест\t", 2))
