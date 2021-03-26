"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
(как быть?); как лучше хранить конфигурацию этого стартера, чтобы в
будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные
о вложенных папках и файлах (добавлять детали)?
"""

import os


def get_offset(line):
    cnt = 0
    try:
        while line[cnt] == ' ':
            cnt += 1
    except IndexError:
        pass
    return cnt


def read_config(config_filename):
    with open(config_filename, 'r', encoding='utf-8') as f:
        config = f.readlines()
    return config


def get_file_structure(config):
    folders = {}
    if len(config) > 0:
        first_line = config[0]
        for line in config[1:]:
            if get_offset(line) < get_offset(first_line):
                raise ValueError('Неравильные отступы')

        start_line_num = 0
        line_num = 1
        while line_num < len(config):
            line = config[line_num]
            if get_offset(line) == get_offset(first_line):
                dirname = config[start_line_num].strip()
                folders[dirname] = get_file_structure(config[start_line_num+1:line_num])
                start_line_num = line_num
            line_num += 1
        dirname = config[start_line_num].strip()
        folders[dirname] = get_file_structure(config[start_line_num + 1:line_num])

    return folders


def build_folders_tree(path, folders):
    for folder, children in folders.items():
        full_dirname = os.path.join(path, folder)
        if os.path.isdir(full_dirname):
            pass
        else:
            os.mkdir(full_dirname)
        build_folders_tree(full_dirname, children)


config = read_config('config.txt')
folders = get_file_structure(config)
build_folders_tree('structure', folders)
