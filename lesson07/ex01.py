"""
Реализовать класс ​ Matrix ​ (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()​ ), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода ​ __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода ​ __add__() для реализации операции сложения двух
объектов класса ​ Matrix ​ (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:

    def __init__(self, list_of_lists):
        length = len(list_of_lists[0])
        if all(len(lst) == length for lst in list_of_lists[1:]):
            self.contain = list_of_lists
        else:
            raise ValueError('Lists have different sizes. \nImpossible to create matrix')

    def __str__(self):
        string = ''
        for i in range(len(self.contain)):
            for j in range(len(self.contain[0])):
                string += "{:4d}".format(self.contain[i][j])
            string += '\n'
        return string

    def __add__(self, other):
        # checks if both matrices are the same sizes
        if len(self.contain) != len(other.contain) or len(self.contain[0]) != len(other.contain[0]):
            return 'Matrices have different sizes. \nImpossible to add'
        for i in range(len(self.contain)):
            for j in range(len(self.contain[0])):
                self.contain[i][j] += other.contain[i][j]
        return self


try:
    matrix = Matrix([[1, 2, 3], [4, 5, 6, 8]]) # error check
except ValueError as e:
    print(e)  # should be exit()

matrix1 = Matrix([[16, 11, 24], [19, 8, 30]])
matrix2 = Matrix([[29, 15, 16], [1, 22, 13]])
print(matrix1 + matrix2)
