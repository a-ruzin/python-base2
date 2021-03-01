"""
Вам нужны ассоциативные массивы — в Python есть словари
	.keys()
	.values()
	.items()
	Словари: .get() и .setdefault()
	Словари: .update() и .popitem()
	Словари: цикл for in
"""

# a = ['Лутц', 'Бизли', 'Ромальо']
# a[0]
# for author in a:
#     if 'Л' == author[0]:
#         pass


# a = {'Л': ['Лутц'], 'Б': ['Бизли', 'Боб'], 'Р': ['Ромальо']}
#
# print(a['Л'])

# hashmap

# Автор книга цена
# books = [
#     'Лутц Питон 100',
#     'Бизли СправочникПитон 150',
#     'Ромальо Забыл 200',
# ]
#
# person = {'name': 'Вася', 'position': 'Директор', 'salary': 100}
#
# person['birthday'] = '1.1.1990'

# values = list(person.items())
#
# person2 = dict(person.items())
# person3 = dict(values)
#
# print(person2, id(person2))
# print(person3, id(person3))
#
# values = list(person.items())
# print(values)

# print(person.get('preferable_color', 'red'))

# # 1) модификация внутреннего состояния
# # 2) расчет значение и возврат результата
#
# print(person.setdefault('name', 'red'))
#
# print(person)
# key, value = person.popitem()
# print(person)
#
# for key, value in person.items():
#     print(key, value)
#
# person[4] = None
# print(4 in person)
# person[tuple(books)] = 'asdf'
# print(person)


# books = [
#     'Лутц Питон 100',
#     'Лутц Питон2 110',
#     'Бизли СправочникПитон 150',
#     'Бизли СправочникC++ 350',
#     'Ромальо Забыл 200',
# ]
#
# store = {}
# for book in books:
#     author, title, price = book.split()
#     store.setdefault(author, [])
#     store[author].append({'title': title, 'price': price})
#
# import pprint
# pprint.pprint(store)
#
# for author in sorted(store.keys(), reverse=True):
#     print(author, store[author])


# ======================
# Что такое функция в Python
# 	Документирование кода функций
# 		Одна строка
# 		Несколько строк
# Области видимости переменных
#
# Продвинутая работа с аргументами функций
# 	Позиционные аргументы и *args
# 	Необязательные аргументы
# 	Именованные аргументы и **kwargs


# def calc_cube(param):
#     cube = param ** 3
#     return cube

# def calc_sum_of_digits(number):
#     sum_of_digits = 0
#     while number > 0:
#         sum_of_digits += number % 10
#         number //= 10
#     return sum_of_digits
#
#
# text = input('Введите число: ')
# while text != '0':
#     number = int(text)
#     sum_of_digits = calc_sum_of_digits(number)
#     print(sum_of_digits)
#     text = input('Введите число: ')


# 1) модификация внутреннего состояния
# 2) расчет значение и возврат результата

# person = {'name': 'Вася', 'position': 'Директор', 'salary': 100}
#
# TOO_MUCH = 300
#
#
# def calc_new_salary(prsn, increment, multiplier=1.0, multiplier2=1.0, multiplier3=1.0):
#     """
#     Функция считает навое значение оклада
#
#     :param prsn: Словарь
#     :param increment: размер прибавки
#     :return: новое значение з.п.
#     """
#     new_salary = prsn['salary'] + increment * multiplier
#     return new_salary
#
#
# def increase_salary(person, increment):
#     person['salary'] += increment
#
#
# print(calc_new_salary(person, 100, multiplier3=1.5))


# if calc_new_salary(person, 100) <= TOO_MUCH:

#
#
# def my_print(b, a, *args, key=None, **kwargs):
#     print(f'Вы передали {len(args)} аргументов')
#     print(args[3], type(args))
#     print(kwargs, type(kwargs))
#
# my_print(2,1,3,4,2,3,4,4,5, key='asdf', setting1=344, xxxxx=34)

import random

# randrange(), randint(), choice()

# for x in range(10):
#     print(x, random.randrange(1, 10, 2))

# lst = list(range(10))
# print(lst)
# print(random.choice('print(random.choice'))
#

lst = []
for x in range(10):
    lst.append(random.randint(1, 100))

print(lst)


# def check_if_number_is_odd(value):
#     return value % 2 == 1
#
#
# def check_if_number_square(value):
#     x = int(value ** 0.5)
#     return value == x * x
#
#
# result = list(filter(check_if_number_is_odd, lst))
# print(result)
#
# result = list(filter(check_if_number_square, lst))
# print(result)

# def calc_square(value):
#     return value * value
#
# result = list(map(calc_square, lst))
# print(result)

# filter(), map(), zip()

# names = ['a', 'b', 'c']
# names2 = ['aa', 'bb', 'cc', 'dd']
#
# result = list(zip(names, lst, names2))
# print(result)
# print(random.choice(result))
#

# lambda-функции

result = list(filter(lambda v: v % 2 == 1, lst))
print(result)
