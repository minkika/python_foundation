"""
Реализовать базовый класс ​ Worker ​ (работник), в котором определить атрибуты: ​
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс ​ Position ​ (должность) на базе класса ​ Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса ​ Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    _income = {'wage': 0, 'bonus': 0}
    name = None
    surname = None

    def __init__(self, name, surname, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus
        self.name = name
        self.surname = surname

class Position(Worker):
    position = None

    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, wage, bonus)
        self.position = position

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_salary(self):
        return sum(self._income.values())


worker = Position('John', 'Taylor', 'manager', 8000, 500)
print(worker.get_full_name())
print(worker.position)
print(worker.get_salary())
