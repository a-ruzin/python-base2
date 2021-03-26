"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import math
import os
from collections import defaultdict


stats = {}
stats2 = defaultdict(lambda: 0)
for dirname, subdirs, filenames in os.walk('../../'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        stat = os.stat(full_path)
        size = 10 ** math.ceil(math.log(stat.st_size, 10))

        stats.setdefault(size, 0)
        stats[size] += 1

        stats2[size] += 1

print (stats)
print (stats2)
