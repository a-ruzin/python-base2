#
# def func(x):
#     y = x ** 2
#     print(y)
#     return y
#
#
# xxx = lambda x: x ** 2
#
# print(xxx(3), xxx.__name__)
#
# print(list(map(lambda x: x ** 2, [1, 2, 3, 5])))
# print(list(map(lambda x: x ** 2, [3, 2, 1, 5])))
#
#
# def prove(xxx):
#     print(xxx)

import re

re_i = re.compile('^.$')

for i in range(100):
    m = re_i.match(str(i))
    print(m)
