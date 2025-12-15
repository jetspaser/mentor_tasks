"""
Реализовать функцию. Функция на вход принимает список list[int] произвольной длины.
Печатает в консоль наименьшее и наибольшее УНИКАЛЬНОЕ число из начального списка.
"""
def print_unique_min_max_set(values: list[int]) -> None:
    """
    Печатает минимальное и максимальное уникальные значения списка.
    """
    unique_values: set[int] = {value for value in values}

    if unique_values:
        print(min(unique_values), max(unique_values))
    else:
        print("Список пуст")


if __name__ == "__main__":
    test_data: list[int] = [3, 1, 2, 3, 5, 1]

    print_unique_min_max_set(test_data)
    print_unique_min_max_set([])
