"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
"""

from re import compile


class CheckList(ValueError):
    def __init__(self, txt):
        self.txt = txt


result = []
pattern = compile('^(0$|-?[1-9]\d*(\.\d*[1-9]$)?|-?0\.\d*[0-9])$')

while True:

    a = input('New element: ')
    if a == 'q':
        break
    try:
        if not pattern.fullmatch(a):
            raise CheckList('Not a number')
    except CheckList as err:
        print(result)
        continue
    else:
        result.append(float(a))
        print(result)
