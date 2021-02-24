"""
Сумма чисел из списка *
Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):

1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
сумма цифр которых делится нацело на 7.

3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
"""

cubes = []
number = 1
while number < 1000:
    cubes.append(number**3)
    number += 2

sum_of_magic_numbers = 0
for number in cubes:
    sum_of_digits = 0
    tmp = number
    while tmp > 0:
        sum_of_digits += tmp % 10
        tmp //= 10

    if sum_of_digits % 7 == 0:
        sum_of_magic_numbers += number

print(sum_of_magic_numbers)


# вторая часть

new_cubes = []
for number in cubes:
    new_cubes.append(number + 17)

sum_of_magic_numbers = 0
for number in new_cubes:
    sum_of_digits = 0
    tmp = number
    while tmp > 0:
        sum_of_digits += tmp % 10
        tmp //= 10

    if sum_of_digits % 7 == 0:
        sum_of_magic_numbers += number

print(sum_of_magic_numbers)


# третья часть

sum_of_magic_numbers = 0

num = 1
while num < 1000:
    number = num**3 + 17

    sum_of_digits = 0
    tmp = number
    while tmp > 0:
        sum_of_digits += tmp % 10
        tmp //= 10

    if sum_of_digits % 7 == 0:
        sum_of_magic_numbers += number

    num += 2

print(sum_of_magic_numbers)
