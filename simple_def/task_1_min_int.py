"""
Реализовать функцию. Функция на вход принимает 2 числа типа int. Печатает в консоль наименьшее из них.
"""
def print_min_number(a: int, b: int) -> None:
    '''
    :param a:
    :param b:
    :return:
    '''
    if a < b:
        print(a)
    else:
        print(b)

# Примеры значений на входе:
print_min_number(5, 10)  # Выведет: 5
print_min_number(7, 3)   # Выведет: 3
print_min_number(4, 4)   # Выведет: 4
