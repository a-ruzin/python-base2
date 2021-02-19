# так выглядит код на python

def calc_hypotenuse(a, b):
    return (a*a + b*b) ** 0.5


# leg_pairs = [[3.0, 4.0], [5.0, 7.0], [13.0, 2.0]]
leg_pairs = [
    [3.0, 4.0],
    [5.0, 7.0],
    [13.0, 2.0],
]

for legs in leg_pairs:
    h = calc_hypotenuse(legs[0], legs[1])
    print(f'Гипотенуза равна {h:.2f} для треугольника с катетами: {legs[0]:.2f} и {legs[1]:.2f}')


#  переменная, тип переменной, оператор ветвления, цикл, функция
