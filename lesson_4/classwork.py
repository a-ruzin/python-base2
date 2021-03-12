# from dir.d2 import f
# from module import a as m_a
#
#
# # print(module.calc_sum(1,2,3,4))
# # print(package.package_function())
# # m_a()
# # p_a()
#
# f()
#
# import requests
# r = requests.get('https://www.geekbrains.ru')
# print(r.status_code, r.content.decode('utf-8'))

# import sys
#
# print('hello', sys.argv)

# import time
#
# start = time.perf_counter()
# j = 0
# for i in range(10000000):
#     j += i
# end = time.perf_counter()
# print(end-start, start, end)
# 1 января 1970 00:00:00


# Модуль datetime: работа с датой и временем
# 	from datetime import datetime
#
# 	date_1 = datetime(year=2020, month=12, day=5)
# 	date_2 = datetime(year=2019, month=12, day=5)
# 	date_delta = date_1 - date_2
# 	print(date_delta.days)  # 366


import datetime

# d1 = datetime.date(2020, 3, 5)
# d2 = datetime.date(2020, 3, 8)
#
# td = d2 - d1
# print(td, type(td), dir(td))
#
# print(td.total_seconds())

# d1 = datetime.date(2020, 3, 5)
# d2 = datetime.datetime(2020, 3, 8, 0, 0, 0)
#
# # if d1 > d2:
# #     print('yes')
#
# # td = d2 - datetime.datetime(d1.year, d1.month, d1.day, 0, 0, 0)
# # print(td, type(td), dir(td))
# #
# # print(td.total_seconds())
# print(datetime.date.today())
# print(datetime.datetime.now())
