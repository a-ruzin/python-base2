"""
Задание 4. Модуль utils
Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:

если используется функция из 2-го задания:
USD 75.18
EUR 80.35
либо, если используется функция из 3-го задания
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""

from utils import get_currency_rate


for currency in ['USD', 'EUR']:
    currency_rate, course_date = get_currency_rate(currency)
    print(f'{currency} {currency_rate}, {course_date}')
