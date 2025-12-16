"""
Реализовать функцию. Функция на вход принимает список list[int] произвольной длины.
Печатает в консоль наименьшее и наибольшее УНИКАЛЬНОЕ число из начального списка.
"""

def print_unique_min_max_set(values: list[int]) -> None:
    """
    :param values: произвольный список чисел
    :return: None
    """

    unique_values: set[int] = {value for value in values if values.count(value) == 1}

    if unique_values:
        print(min(unique_values), max(unique_values))
    else:
        print("Список пуст")

print_unique_min_max_set([3, 1, 2, 3, 5, 1, 6, 6])
