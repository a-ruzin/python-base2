"""
Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".
"""

text = input('Введите число: ')
while text != '0':
    number = int(text)
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    print(sum_of_digits)
    text = input('Введите число: ')
