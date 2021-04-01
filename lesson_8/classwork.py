import re

# values = ['abd4кириллица', 'a3a94237-4987123', '123', '+111', '-+111', '']
#
# for value in values:
#
#     # string = "asdfkj 'a'\\ \"C\" askdj \\fkj    \n"
#
#     # result = re.search(r"a", value)   #  'a' in value
#     # result = re.search(r"\d", value)   #  '0' in value or '1' in value or ... '9' in value
#     # result = re.search(r"[aef8]", value)   #  'a' in value or 'e' in value or ... '8' in value
#     #
#     result = re.search(r"^.$", value)   #
#     # result = re.search(r"(\d)+", value)
#
#     # result = '0' in value or '1' in value or '2' in value
#
#     if result:
#         a, b = result.span()
#         print(value, value[a:b], result.groups())
#     else:
#         print(value, result, 'паттерн не найдено')


text = """
Бухгалтер нашел итоговые показатели.
Валовая прибыль — 5 000 000 руб.((12 000 000 — 2 000 000) – (6 000 000 — 1 000 000)).
Прибыль от продаж — 3 500 000 руб.(5 000 000 — 1 500 000).
Прибыль до налогообложения — 3 000 000 руб.(3 500 000 — 500 000).
Чистая прибыль — 2 400 000 руб.(3 000 000 — 600 000).
Бухгалтер заполнил отчет о финрезультатах так, как показано в таблице 2.
"""

# x = 3
# re_ = f'(0{{{x}}})'
# print(re_)
#
# two_numbers = re.compile(re_)
#
# result = two_numbers.sub(r'"\1"', text)
# print(result)

# re.compile() — компилируем паттерн
# re.match() — ищем с начала строки
# re.fullmatch() — проверяем полное совпадение строки
# re.search() — ищем по всей строке до совпадения
# re.findall() — ищем все совпадения и получаем список
# re.finditer() — итератор всех совпадений
# re.split() — разделяем строку по паттерну
# re.sub() — заменяем совпадения с паттерном

# print(two_numbers.split(text))



#  Декораторы


def validate_frist_argument(func):

    def inner_func(*args, **kwargs):
        print('args:', args, 'kwargs:', kwargs)
        if not isinstance(args[0], int) or not isinstance(args[1], int):
            raise ValueError('Нужно первым аргументом передавать 3')
        res = func(*args, **kwargs)
        print('result', res)
        return res

    return inner_func


@validate_frist_argument
@validate_frist_argument
@validate_frist_argument
def my_sum(a, b):
    return a + b


@validate_frist_argument
def my_mult(a, b):
    return a * b


my_sum(5, 4)
my_mult(3, 4)

# result = get_inner_func(my_sum)
# print(result(3, 4))

# print(my_sum(1, 2), type(my_sum))
