# import os

# from utils.helpers import print_current_work_dir

# print(os.path.curdir)
#
# print(os.path.abspath(os.path.curdir))

# open('utils/file.txt')
# print('asdf')

# /Users/ruzin/Projects/Teaching/python-base2/lesson_7/classwork.py
# c:\Users\User1\...

# classwork.py


# import os
# print(os.listdir())
#
# os.path.curdir
#
# 	abspath() — возвращает абсолютный путь;
# 	basename() — возвращает имя файла из абсолютного или относительного пути;
# 	dirname() — возвращает имя (путь) папки, в которой расположен файл;
# 	split() — делит путь к файлу на путь к папке и имя файла (заменяет вызов двух предыдущих функций);
# 	relpath() — определяет путь к файлу относительно другой папки, не обращается к реальной файловой системе, чисто вычисления (полезна при сохранении путей к файлам в базе данных относительно заданного корня);
# 	join() — склеивает путь из частей (надеемся, вы не делаете это через строки!);
# 	exists() — проверяет существование объекта файловой системы.
# 	isdir()
# 	isfile()
# 	islink()

# print(os.path.abspath('file.txt'))
# print(os.path.abspath('./file.txt'))
# print(os.path.abspath('../file.txt'))
# print(os.path.abspath('utils/file.txt'))
from lesson_7.utils.helpers import print_current_work_dir, func

TMP_DIR = '/tmp/my_tmp_files'

# with open(f'{TMP_DIR}/file.txt', 'r', encoding='utf-8') as f:
#     print(f.read())
#
#
# with open('./file.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

import sys
import os


# print(sys.argv[1])
# print(os.path.relpath(sys.argv[1]))

# path_list = ['/', 'tmp', 'my_files']
#
# for i in range(10):
#     tmp_file_name = os.path.join(*path_list, str(i))   # join('/', 'tmp', 'my_files', str(i))
#     print(tmp_file_name)
#
# 	exists() — проверяет существование объекта файловой системы.
# 	isdir()
# 	isfile()
# 	islink()

#
# for i in range(10):
#     tmp_file_name = os.path.join('tmp', str(i))   # join('/', 'tmp', 'my_files', str(i))
#     print(tmp_file_name, os.path.isdir(tmp_file_name))

# os.mkdir('tmp/3')
# os.mkdir('tmp/3/6')
# os.mkdir('tmp/3/6/7')

# os.makedirs('tmp/4/6/2/3/4/5')

# os.rmdir('tmp/4')

# os.removedirs('tmp/4/6/2/3/4/5')

# os.removedirs('tmp/4/6/7')

# print(os.listdir('tmp'))

# for cdir, subdirs, files in os.walk('..'):
#     for file in files:
#         print(os.path.abspath(os.path.join(cdir, file)))

# from utils.helpers import print_current_work_dir
#
# print_current_work_dir()


# shutil
#
# 	copy
# 	copytree
# 	disk_usage
# 	get_archive_formats
# 	move
# 	rmtree

#
# import shutil
#
# shutil.rmtree('tmp')




# Exceptions
# -------------------------------

def d():
    filename = 'classwork.py'
    try:
        file = open('file.txt', 'wb')
        print('haha')
        func(3)
        print('hoho')
    except ValueError as e:
        print(f'value error')
    except Exception as e:
        print(f'оюбщая ошибка', str(e))
    else:
        print('Все прошло хорошо без ислключений')
    finally:
        file.close()
        print('finally')
    print(f'все хорошо')

try:
    d()
except:
    print('d поймана')

# EAFP   Easy Ask For Forgiveness than Permission
