"""
1. Реализовать класс Matrix (матрица).
Конструктор класса __init__() должен принимать список списков чисел для задания
превоначального состояния матрицы.
Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

В методе __init__() надо проверить корректность передаваемых данных - все списки должны быть одинаковой длины.
В случае расхождения выбрасывать исключение ValueError с соответствующим описанием.
Добавить метод __add__() сложения двух матриц. Складывать можно матрицы одинаковой размерности.
В случае, когда пользователь пытается сложить матрицы разных размеров выбросить исключение ValueError.
В результате сложения двух матриц должна образоваться новая матрица размером N x M,
где каждый элемент в ячейке i,j образован сложением значений из соответствующих ячеек исходных матриц.
Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6", отводя под числа по три разряда,
чтобы для небольших чисел матрица выглядела как таблица.
Создать три матрицы (две одинаковые по размеру и одну с другим размером).
Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат сложения.
"""


class Matrix:
    def __init__(self, rows):
        if len(rows) == 0 or len(rows[0]) == 0:
            raise ValueError('Количество колонок и строк в матрице не должно быть нулем')

        length = None
        for row in rows:
            if length is not None and length != len(row):
                raise ValueError('Строки в матрицы должны быть одинаковой длины')
            length = len(row)

        self.rows = rows

    @property
    def size(self):
        return len(self.rows), len(self.rows[0])

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError('Для сложения матрицы должны быть одинакового размера')

        rows = [
            [
                self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[i]))
            ] for i in range(len(self.rows))
        ]

        # rows = []
        # for i in range(len(self.rows)):
        #     row = []
        #     for j in range(len(self.rows[i])):
        #         row[j] = self.rows[i][j] + other.rows[i][j]
        #     rows.append(row)

        return Matrix(rows)

    def __str__(self):
        return '\n'.join(
            " ".join(
                f'{value:3}' for value in row
            )
            for row in self.rows
        )


m = Matrix([[1,2,3], [4,5,6]])
print('m', m.size)
print(m)
print('---')

m2 = Matrix([[3,3,3], [2,2,2]])
print('m2', m2.size)
print(m2)
print('---')

m3 = Matrix([[99,99], [99,99], [99,99]])
print('m3', m3.size)
print(m3)
print('---')

m4 = m + m2
print('m4')
print(m4)
print('---')
print('m')
print(m)
print('---')
print('m2')
print(m2)
print('---')


m5 = m + m3
print('m5')
print(m5)
print('---')
