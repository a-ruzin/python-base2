"""
Задание 5
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп.
Например:
57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...

Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).

Создать новый список, содержащий те же цены, но отсортированные по убыванию.

Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих
товаров по возрастанию, написав минимум кода?

Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

prices = [
    12.23, 34.98, 99.12, 99.78, 93.7, 12.25, 34.98, 89.12, 89.78, 93.01,
    32.23, 54.98, 59.12, 19.78, 3.00, 2.23, 3.9, 79.12, 39.78, 63.70,
]

print(id(prices))
prices.sort()
print(id(prices))

prices_to_print = []
for price in prices:
    rubles = int(price)
    kopeeks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopeeks:02} коп')
print(', '.join(prices_to_print))

print('-------')

new_prices = sorted(prices, reverse=True)
prices_to_print = []
print(id(new_prices))
for price in new_prices:
    rubles = int(price)
    kopeeks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopeeks:02} коп')
print(', '.join(prices_to_print))

print('-------')

prices_to_print = []
for price in prices[-5:]:
    rubles = int(price)
    kopeeks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopeeks:02} коп')
print(', '.join(prices_to_print))
