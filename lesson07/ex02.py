"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — ​ одежда​ , которая может иметь определенное название. К
типам одежды в этом проекте относятся ​ пальто ​ и ​ костюм​ . У этих типов одежды существуют
параметры: ​ размер ​ (для ​ пальто​ ) ​ и ​ рост ​ (для ​ костюма​ ). Это могут быть обычные числа: ​
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5)​ , для костюма ​ (2*H + 0.3)​ . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора ​ @property​ .
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def count_material(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def count_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def count_material(self):
        return 2 * self.height + 0.3


coat = Coat('Coat Melany', 36)
print(f'{coat.name} sized {coat.size} requires {coat.count_material:.02f} sq. meters of material')
suit = Suit('Suit Angy', 164)
print(f'{suit.name} for height {suit.height} requires {suit.count_material:.02f} sq. meters of material')
