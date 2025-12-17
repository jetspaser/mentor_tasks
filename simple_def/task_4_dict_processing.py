"""
Task 4. Реализовать функцию. Функция на вход принимает словарь dict[str, int].
Печатает в консоль 2 списка:
1. list[str], каждым значением которого являются keys полученного словаря приведённые к верхнему регистру.
2. list[int], каждым значением которого являются values полученного словаря возведённые:
   - в квадрат - если значение > 5
   - в куб - если значение < 5
"""


def process_dict(data: dict[str, int]) -> None:
    """
    Обрабатывает словарь и выводит два списка.

    :param data: Словарь вида {строка: число}
    :return: None
    """

    # список ключей
    up_keys = []
    for key in data:
        up_keys.append(key.upper())

    # список значений
    accept_values = []
    for value in data.values():
        if value > 5:
            accept_values.append(value ** 2) # возводим в квадрат
        elif value < 5:
            accept_values.append(value ** 3) # возводим в куб
        else:
            accept_values.append(value) # если значение равно 5

    # печатаем результат
    print("Ключи в верхнем регистре:", up_keys)
    print("Обработанные значения:", accept_values)

process_dict({"Пиво": 25, "Шашлык": 15, "Лаваш": 4, "Зелень": 5})
