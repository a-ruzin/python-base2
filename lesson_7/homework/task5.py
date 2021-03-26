"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки
в виде словаря, в котором ключи те же, а значения — кортежи вида
(<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import math
import os
from collections import defaultdict


stats2 = defaultdict(lambda: [0, set()])
for dirname, subdirs, filenames in os.walk('../../'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        stat = os.stat(full_path)
        size = 10 ** math.ceil(math.log(stat.st_size, 10))
        stats2[size][0] += 1
        segments = filename.split('.')
        if len(segments) > 1:
            ext = segments[-1]
        else:
            ext = ''
        stats2[size][1].add(ext)

stat = {k: (v[0], list(v[1])) for k, v in stats2.items()}
print(stat)
