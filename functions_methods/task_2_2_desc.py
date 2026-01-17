

from functions_methods.task_2_1_dict import task_2_1

"""
Реализовать функцию с названием task_2_2.
Функция принимает на вход cписок list[list[str]]
содержащий любое количество значений.
В своём теле использует task_2_1 и возвращает список словарей исходных данных,
отфильтрованный по возрасту DESC.
"""

def task_2_2(data: list[list[str]]) -> list[dict[str, str | int]]:
    """
    :param data: список списков, содержащих строковые значения
    :return: список словарей, отсортированных по возрасту (DESC)
    """

    result: list[dict[str, str | int]] = []

    for item in data:
        parsed_data = task_2_1(item)
        result.append(parsed_data)

    return sorted(result, key=lambda x: x["age"], reverse=True)

input_data = [
    ["Алексей-Попов-29"],
    ["Иван-Иванов-18"],
    ["Данила-Козловский-40"]
]

result = task_2_2(input_data)
print(result)
