"""
3. Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные
исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
"""

import os
import shutil

project_path = 'structure2/my_project'
project_templates_path = os.path.join(project_path, 'templates')
try:
    os.mkdir(project_templates_path)
except:
    pass

for dirname in os.listdir(project_path):
    app_template_dir = os.path.join(project_path, dirname, 'templates', dirname)
    if os.path.isdir(app_template_dir):
        shutil.copytree(app_template_dir, os.path.join(project_templates_path, dirname))
