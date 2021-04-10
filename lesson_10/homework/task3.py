"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Эти методы
должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и округление до целого числа деления клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.

Добавить к классу метод print(columns), распечатыващий на экране звездочки рядами
по columns звездочек в одном ряду в количестве равном числу ячеек клетки.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, если в клетке 12 ячеек, а запросили напечатать по 5 звездочек в ряду,
то на экране должно быть:

*****
*****
**
"""


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if other.cells > self.cells:
            raise ValueError('Вычитать можно только из большей клетки меньшую')

        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def print(self, columns):
        # print(self.cells)
        for i in range(self.cells // columns):
            print('*' * columns)
        if self.cells % columns > 0:
            print('*' * (self.cells % columns))


c1 = Cell(10)
print('c1')
c1.print(6)
print('---')

c2 = Cell(21)
print('c2')
c2.print(6)
print('---')


# ++++
c3 = c1 + c2
print('c3')
c3.print(6)
print('---')

c1 = Cell(10)
print('c1')
c1.print(6)
print('---')

c2 = Cell(21)
print('c2')
c2.print(6)
print('---')


# ----
try:
    c4 = c1 - c2
except ValueError as e:
    print(e)
else:
    print('c4 ++++')
    c4.print(6)
    print('---')

c5 = c2 - c1
print('c5')
c5.print(6)
print('---')

c6 = c2 * c1
print('c6')
c6.print(6)
print('---')

c6 = c2 * c1
print('c6')
c6.print(30)
print('---')

c6 = c2 * c1
print('c6')
c6.print(15)
print('---')

c7 = c2 / c1
print('c7')
c7.print(6)
print('---')