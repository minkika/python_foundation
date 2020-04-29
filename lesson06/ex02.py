"""
Реализовать класс ​ Road ​ (дорога), в котором определить атрибуты: ​ length ​ (длина), ​
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    __length = 0
    __width = 0
    height = 5
    cost = 1000
    weight = 25
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calculate (self):
        return self.__length * self.__width * self.weight * self.height
    def costs(self):
        return self.calculate() * self.cost

road1 = Road(1500,18)
print(f'This road requires {road1.calculate()} tons of bitum')
print(f'...and {road1.costs()} dollars')