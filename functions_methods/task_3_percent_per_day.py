

"""
Реализовать функцию с названием task_3.
Функция принимает на вход четыре параметра percent_per_day: float - проценты в день,
 wonted: float - желаемая сумма, first_input: float - первоначальная сумма.

 Функция выводит, за сколько дней удалось получить нужную сумма, учитывая,
 что проценты НЕ начисляются в дни кратные 6 и 7
 В выводе использовать f -строки. "Количество дней: Итоговая сумма, округлённая до 2-х символов:"
"""

def task_3(percent_per_day: float, wonted: float, first_input: float) -> None:
    """
    :param percent_per_day: ежедневный процентный доход
    :param wonted: желаемая сумма
    :param first_input: начальная сумма
    """

    days = 0
    current_sum = first_input

    while current_sum < wonted:
        days += 1

        if days % 6 != 0 and days % 7 != 0:
            current_sum += current_sum * (percent_per_day / 100)

    print(
        f"Количество дней: {days}. "
        f"Итоговая сумма, округлённая до 2-х символов: {round(current_sum, 2)}"
    )

task_3(percent_per_day = 10, wonted = 2000, first_input = 500)
