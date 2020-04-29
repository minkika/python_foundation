"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""

class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f'{self.r} + {self.i}i'

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return ComplexNumber(self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)


a = ComplexNumber(5, 6)
b = ComplexNumber(5, 6)
print(a + b)
print(a * b)
c = complex(5, 6)
d = complex(5, 6)
print(c + d)
print(c * d)
