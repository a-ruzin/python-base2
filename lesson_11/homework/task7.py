"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число». Реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'({self.real}{self.imag:+}j)'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # (a + bi) * (c + di) => ac - bd + (ad + bc)i
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )


im1 = Complex(5, 1)
im2 = Complex(1)
im3 = Complex(0, 1)

print(im1, im2, im3)

im4 = im1 + im2
print('im4', im4, (5+1j) + 1)

im4 = im1 + im2 + im3
print('im4', im4, (5+1j) + 1 + 1j)

im5 = im4 * im3
print(im5, (6+2j)*(1j))

im6 = im5 * im5
print('im6', im6, (-2+6j)*(-2+6j) )
