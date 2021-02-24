# # так выглядит код на python
#
# def calc_hypotenuse(a, b):
#     return (a*a + b*b) ** 0.5
#
#
# # leg_pairs = [[3.0, 4.0], [5.0, 7.0], [13.0, 2.0]]
# leg_pairs = [
#     [3.0, 4.0],
#     [5.0, 7.0],
#     [13.0, 2.0, 3.0],
# ]
#
# for leg_pair in leg_pairs:
#     if len(leg_pair) == 2:
#         h = calc_hypotenuse(leg_pair[0], leg_pair[1])
#         print(f'Гипотенуза равна {h:.2f} для треугольника с катетами: {leg_pair[0]:.2f} и {leg_pair[1]:.2f}')
#     else:
#         print('Неверное число катетов для треугольника')
# #  переменная, тип переменной, оператор ветвления, цикл, функция
#

a = int(input('введите число:'))
print(type(a))
a = int(a)
b = a + 34
print(type(a), a)
b = str(b)
print(type(b), b)
