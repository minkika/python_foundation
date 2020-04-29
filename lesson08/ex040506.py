"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
"""

class Storage:
    items = {'Printer': 0, 'Scanner': 0}

    def add_item(self, item):
        self.items[item.name] += item.qty

    def move_item(self, item, qty):
        self.items[item] -= qty

    def get_items(self):
        print(self.items)


class StorageItem:

    def __init__(self, qty):
        self.set_qty(qty)

    def set_qty(self, qty):
        if isinstance(qty, int):
            self.qty = qty
        else:
            raise TypeError


class Printer(StorageItem):
    name = 'Printer'


class Scanner(StorageItem):
    name = 'Scanner'


storage = Storage()

storage.add_item(Printer(4))
storage.add_item(Scanner(6))
storage.move_item('Printer', 2)
storage.get_items()
