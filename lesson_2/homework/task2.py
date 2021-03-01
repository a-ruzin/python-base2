"""
Задание 2
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
"""

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# target_list = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

target_list = []
for element in source_list:
    if element.isdigit():
        target_list.extend(['"', f'{int(element):02}', '"'])
    elif (element[0] == '+' or element[0] == '-') and element[1:].isdigit():
        sign = element[0]
        target_list.extend(['"', sign + f'{int(element[1:]):02}', '"'])
    else:
        target_list.append(element)

result = ' '.join(target_list)
print(result)


source_list_index = 0
target_list_index = 0
tmp_list = []
while source_list_index < len(source_list):
    if source_list[source_list_index] == target_list[target_list_index]:
        pass # все хорошо
        element = source_list[source_list_index]
        target_list_index += 1
    else:
        element = "".join(target_list[target_list_index:target_list_index+3])
        target_list_index += 3

    tmp_list.append(element)
    source_list_index += 1

result = ' '.join(tmp_list)
print(result)
