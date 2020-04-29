"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: ​
speed, color, name, is_police (булево). А также методы:go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: ​ TownCar​ , ​ SportCar​ , ​ WorkCar​ , ​ PoliceCar​ . Добавьте в базовый класс метод
show_speed​ , который должен показывать текущую скорость автомобиля. Для классов
TownCar ​ и ​ WorkCar ​ переопределите метод ​ show_speed​ . При значении скорости свыше 60
(​TownCar​ ) и 40 (​ WorkCar​ ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self, speed):
        self.speed = speed
        return f'Car {self.name} is going now'

    def stop(self):
        self.speed = 0
        return f'Car {self.name} stops'

    def turn(self, direction):
        return f'Car {self.name} turned to {direction}'

    def show_speed(self):
        return f'The speed of car {self.name} is {self.speed}'

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Speed warning! Speed limit is 60, your speed is {self.speed}'
        else:
            return f'The speed of car {self.name} is {self.speed}'

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Speed warning! Speed limit is 60, your speed is {self.speed}'
        else:
            return f'The speed of car {self.name} is {self.speed}'


class PoliceCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name, True)

town_car = TownCar('red', 'BMW')
print(town_car.go(70))
print(town_car.turn('left'))
print(town_car.show_speed())
print(town_car.stop())
print(town_car.show_speed())
print(f'Color of {town_car.name} is {town_car.color}')
sport_car = Car('green', 'Alfa Romeo')
print(sport_car.go(320))
print(f'Color of {sport_car.name} is {sport_car.color}')
print(sport_car.turn('left'))
print(sport_car.show_speed())
print(sport_car.stop())
print(sport_car.show_speed())
work_car = WorkCar('orange', 'Mercator')
print(work_car.go(320))
print(work_car.turn('left'))
print(work_car.show_speed())
print(work_car.stop())
print(work_car.show_speed())
print(f'Color of {work_car.name} is {work_car.color}')
police_car = PoliceCar('blue', 'Cops')
print(police_car.go(90))
print(f'Color of {police_car.name} is {police_car.color}')
print(police_car.turn('left'))
print(police_car.show_speed())
print(police_car.stop())
print(police_car.show_speed())
