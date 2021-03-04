"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
"""


def thesaurus(*args):
    dictionary = {}
    for full_name in args:
        first_name, last_name = full_name.split()
        first_letter_of_first_name = first_name[0]
        first_letter_of_last_name = last_name[0]
        dictionary.setdefault(first_letter_of_last_name, {}).\
            setdefault(first_letter_of_first_name, []).append(full_name)
    return dictionary


d = thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
for first_letter_of_last_name in sorted(d.keys()):
    print(first_letter_of_last_name)
    for first_letter_of_first_name in sorted(d[first_letter_of_last_name].keys()):
        print(f'  {first_letter_of_first_name}: {d[first_letter_of_last_name][first_letter_of_first_name]}')
