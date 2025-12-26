

"""
Реализовать функцию с названием task_2_1.
Функция принимает на вход список list[str], содержащий  одно значение.
Значение списка представляет собой строку вида: "Алексей-Попов-29"

Функция должна возвращать dict[str, str | int] значение в соответствии со следующим примером:
"Алексей-Попов-29" -> {"first_name": "Алексей", "last_name": "Попов", "age": 29}
"""

def task_2_1(data: list[str]) -> dict[str, str | int]:
    """
    :param data: список с одним строковым значением
    :return: словарь с ключами 'first_name', 'last_name', 'age'
    """

    # Получаем строку из списка
    value = data[0]

    # Разбиваем строку по дефису
    first_name, last_name, age = value.split("-")

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": int(age)
    }

result = task_2_1(["Алексей-Попов-29"])
print(result)
