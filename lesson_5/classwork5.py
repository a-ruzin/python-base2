

# O(N)    C1*N*N          C1*M*M

# def gen_odd_numbers(limit):
#     number = 1
#     while number < limit:
#         yield number
#         number += number
#
#
# values = list(gen_odd_numbers(10000))
# print(values)

# def gen_round(lst, limit=10):
#     counter = 0
#     while True:
#         for i in lst:
#             if counter >= limit:
#                 return
#             yield i
#             counter += 1
#
# for i in gen_round([1,2,3,5,6], 20):
#     print(i)

# g1 = gen_odd_numbers()
# g2 = gen_odd_numbers()
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g2))
# print(next(g1))
# print(next(g2))

# except StopIteration:
#     pass
# print(values)


# for i in gen_odd_numbers():
#     print(i)
#
#
# for i in range(1, 100, 25):
#     print(i)
#
# values = []
# for i in range(5):
#     values.append(2**i)
#
# print(values)

# values = []
# for i in range(1, 21):
#     values.append(i*i)
#
# print(values)
#
# values = [i*i for i in range(1, 21) if (i+1) % 3 == 0]
#
# print(values)

# names = ["Петя", "Маша", "Оля", "Ваня", "Вася"]
#
# values = {name[0]: [name] for name in names}
# print(values)
#
# values = {}
# for name in names:
#     values.setdefault(name[0], []).append(name)
#
# print(values)

# ["Вася", "Петя", "Маша", "Оля", "Ваня"]

#
# new_set = {1, 2, 3, 4, 5, ['О', 1]}
#
#
# names = ["Петя", "Маша", "Оля", "Ваня", "Вася"]
#
# new_set2 = {name[0] for name in names}
# print(new_set2)
#
# lst = [1,2,3,4, 1,2,3,4]
# new_set3 = set(lst)
#
# print(new_set2 | new_set)
#

# names = ["Петя", "Маша", "Оля", "Ваня", "Вася"]
# names2 = ["Оля", "Женя", "Вася", "Петя"]
#
# result = list(set(names) - set(names2))
# print(result)

# def calculate(num):
#     # очень сложные вычисления
#     print('calc', num)
#     return num*num
#
#
# numbers = (calculate(i) for i in range(1, 20))
#
# accumulator = 0
# for i, val in enumerate(numbers, start=1):
#     print(i, val)
#     accumulator += val
#     if accumulator > 100:
#         break
#
# print(accumulator)

from urllib.request import urlopen
from xml.etree import ElementTree as etree

def get_currency_rate(cur):
    return rates.get(cur)

cur = ['USD', 'EUR']

rates = {}
with urlopen("http://www.cbr.ru/scripts/XML_daily.asp") as r:
    el = etree.parse(r)
    root = el.getroot()

    for currency in cur:
        rate = el.findtext('.//Valute[CharCode="'+currency+'"]/Value')
        rate = float(rate.replace(',', '.'))
        rates[currency] = rate


for c in cur:
    print(c, get_currency_rate(c))
