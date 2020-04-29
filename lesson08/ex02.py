"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""

class DivisionLawlessness(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    return a / b


while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        if b == 0:
            raise DivisionLawlessness("Do not divide by zero, please. ")
    except ValueError:
        print("Not a number. ")
    except DivisionLawlessness as err:
        print(err)
    else:
        print(div(a, b))
        break
