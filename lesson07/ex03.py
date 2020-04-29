"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (​ __add__()​ ), вычитание (​ __sub__()​),
умножение (​ __mul__()​ ), деление (​__truediv__()​ ). Данные методы должны применяться ​ только
к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться округление
значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод ​ make_order()​ , принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида ​ *****\n*****\n*****​ ..., где количество ячеек между ​
\n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() ​ вернет строку: ​ *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() ​ вернет строку: ​ *****\n*****\n*****.
"""


class Cell:
    __cell_count = 0
    _nucleus = 0

    def __init__(self, nucleus):
        Cell.__cell_count += 1
        self.nucleus = nucleus

    @property
    def counter(self):
        return self.__cell_count

    def __add__(self, other):
        return Cell(self._nucleus + other._nucleus)

    def __sub__(self, other):
        if self._nucleus < other._nucleus:
            print('Nothing')
        else:
            return Cell(self._nucleus - other._nucleus)

    def __mul__(self, other):
        return Cell(self._nucleus * other._nucleus)

    def __truediv__(self, other):
        if other._nucleus == 0:
            print('Nothing')
        else:
            return Cell(round(self._nucleus / other._nucleus))

    def __str__(self):
        return str(f'Cell contains {self._nucleus} nucleus')

    def make_order(self, nucleus_per_row):
        if int(nucleus_per_row) <= 0:
            return "Nothing"
        else:
            order = ''
            for i in range(1, self._nucleus):
                if i % nucleus_per_row == 0:
                    order += '*\n'
                else:
                    order += '*'
            return order

    @property
    def nucleus(self):
        return self._nucleus

    @nucleus.setter
    def nucleus(self, amount):
        if amount <= 0:
            self._nucleus = 0
        else:
            self._nucleus = amount

    def fill(self, amount):
        self._nucleus += amount


def sep():
    print('=' * 15)


cell_1 = Cell(-9)  # check_setter, should be 0
print(cell_1)  # 0 + check str
cell_1.fill(10)  # check_fill
print(cell_1)  # 10
cell_2 = Cell(20)
print(cell_2)  # 20
cell_3 = cell_1 + cell_2  # add
print(cell_3)  # 30
cell_3 = cell_1 - cell_2  # sub, error
print(cell_3)  # None
cell_3 = cell_2 - cell_1  # sub
print(cell_3)  # 10
cell_1.fill(-10)  # to be zero
print(cell_1)  # 0
cell_3 = cell_2 * cell_1  # mul zero
print(cell_3)  # 0
cell_1.fill(10)  # not to be zero
print(cell_1)  # 10
cell_3 = cell_2 * cell_1  # mul
print(cell_3)  # 200
cell_1.fill(-10)  # to be zero
print(cell_1)  # 0
cell_3 = cell_2 / cell_1  # div, error
print(cell_3)  # None
cell_1.fill(11)  # not to be zero
print(cell_1)  # 11
cell_3 = cell_2 / cell_1  # div
print(cell_3)  # 20/11
print(cell_1.make_order(5))
sep()
print(cell_1.make_order(3))
sep()
print(cell_1.make_order(2))
sep()
print(cell_1.make_order(1))
sep()
print(cell_1.make_order(0))
